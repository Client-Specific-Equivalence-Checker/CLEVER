from pyexsmt import uninterp_func_pair
from pyexsmt.loader import *
from pyexsmt.explore import ShadowExplorationEngine
import time

from pysmt.shortcuts import *

PATTERN = 0
SOLVER = 1
NOTCSE = 2
COUNTER = 3
ERROR = 4

def prove_cse(strategy, file1, file2, client, library):
    if strategy == "LAZY":
        lazy = True
    else:
        lazy = False
    orig = loaderFactory(file1, client)
    if orig is None:
        sys.exit(1)

    upgr = loaderFactory(file2, client)
    if upgr is None:
        sys.exit(1)

    unknown = Symbol('Unknown', INT)
    try:
        starttime_wall = time.time()
        
        solver = Solver("z3")
        engine = ShadowExplorationEngine(orig.create_invocation(), upgr.create_invocation(), solver)
        result_struct = engine.explore([], lazy)

        if isinstance(result_struct, tuple):
            orig_struct = result_struct[0]
            upgr_struct = result_struct[1]
            orig_summary = orig_struct.to_summary(unknown)
            upgr_summary = upgr_struct.to_summary(unknown)
        else:
            endtime_wall = time.time()
            exec_time = endtime_wall-starttime_wall
            return COUNTER, result_struct, exec_time

        if orig_summary == upgr_summary:
            endtime_wall = time.time()
            exec_time = endtime_wall-starttime_wall
            print("Summary:\n%s" % orig_summary)
            print("#Paths: %d" % len(orig_struct.generated_inputs))
            return PATTERN, None, exec_time

        assertion = EqualsOrIff(orig_summary, upgr_summary)
        sat = get_model(Not(assertion), "z3")
        endtime_wall = time.time()
        exec_time = endtime_wall-starttime_wall
        print("Attempting to Prove:\n%s" % assertion)
        print("#Paths V1: %d" % len(orig_struct.generated_inputs))
        print("#Paths V2: %d" % len(upgr_struct.generated_inputs))
        if sat:
            return NOTCSE, sat, exec_time
        else:
            return SOLVER, sat, exec_time

    except (ImportError, NotImplementedError, TypeError) as error:
        # create_invocation can raise ImportError
        # Some operators are not implemented.
        # Don't need a stack trace for this.
        logging.error(error)

    return ERROR, None, 0
