
from pyexsmt import uninterp_func_pair
from pyexsmt.loader import *
from pyexsmt.explore import ExplorationEngine

from pysmt.shortcuts import *

PATTERN = 0
SOLVER = 1
NOTCSE = 2
ERROR = 3

def prove_cse(startegy, file1, file2, client, library):
    orig = loaderFactory(file1, client)
    if orig is None:
        sys.exit(1)

    upgr = loaderFactory(file2, client)
    if upgr is None:
        sys.exit(1)

    unknown = Symbol('Unknown', INT)
    try:
        orig_engine = ExplorationEngine(orig.create_invocation())
        orig_struct = orig_engine.explore()
        orig_summary = orig_struct.to_summary(unknown)
        print(serialize(orig_summary))

        upgr_engine = ExplorationEngine(upgr.create_invocation())
        upgr_struct = upgr_engine.explore()
        upgr_summary = upgr_struct.to_summary(unknown)
        print(serialize(upgr_summary))

        assertion = EqualsOrIff(orig_summary, upgr_summary)
        print("Attempting to Prove:\n%s" % serialize(assertion))
        assertion = Not(assertion)
        model = get_model(assertion)
        if model:
            return NOTCSE, model
        else:
            return SOLVER, None
        return ERROR, None

    except (ImportError, NotImplementedError, TypeError) as error:
        # create_invocation can raise ImportError
        # Some operators are not implemented.
        # Don't need a stack trace for this.
        logging.error(error)
        return ERROR, None
