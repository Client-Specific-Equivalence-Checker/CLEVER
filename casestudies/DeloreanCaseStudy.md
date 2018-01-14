# [Delorean](https://github.com/myusuf3/delorean) Case Study : 100 Most Recent Commits

## Results

### General Stats
- 5/100 commits contained semantic changes to a function that did not modify signature.
    - This excludes changes to tests, and one big batch interface change whose individual components could have been chosen (see notes).
- 6 libraries were identified (1 commit contained 2 candidate libraries)
- 0 clients were found inside of project for these 6 libraries.
    - Delorean is really meant to be a library
- There were a lot of duplicate commits, and most commits were changes to documentation.

### Client-Specific Equivalence Checking
I Searched "Delorean" on Github. This yielded 1307 Python code results.
I looked at the first 200 code results.
Out of those 200 I ignored code results that were calling a different Delorean project, were the Delorean project (or a fork/copy), or had less than 5 stars on Github.
This resulted in 9 projects that depend on Delorean, of those 9, the following actually used the libraries identified earlier (not for testing).
- https://github.com/amicks/Speculator
- https://github.com/numberoverzero/bloop
- https://github.com/biicode/bii-server
- https://github.com/mwaterfall/alfred-datetime-format-converter
- https://github.com/myusuf3/courtside

I then searched through each of the 9 projects to find clients for each of the 6 library functions we identified below (in progress).

Note: should follow the clients of init further. They usually return the object.

#### Speculator
- [ ] stops
- [ ] \_\_eq\_\_
- [x] \_\_init\_\_
    -  [many inits, date_to_delorean, date_to_epoch, now_delorean, get_end_start_epochs](https://github.com/amicks/Speculator/blob/17ac7a1c0a2df8370e2820b98ff13af489b666b0/speculator/utils/date.py)
- [ ] parse
- [ ] end\_of\_day()
- [ ] naive

#### bloop
- [ ] stops
- [ ] \_\_eq\_\_
- [x] \_\_init\_\_
    - [DateTime.dynamo_load, Timestamp.dynamo_load](https://github.com/numberoverzero/bloop/blob/a19c410845d877e32a48ffec1d9d82cb2d7ae31b/bloop/ext/delorean.py) 
    - [new_expiry](https://github.com/numberoverzero/bloop/blob/a19c410845d877e32a48ffec1d9d82cb2d7ae31b/examples/mixins.py)
- [ ] parse
- [ ] end\_of\_day()
- [ ] naive


#### bii server
[all here. Follow UtcDatetime to get more clients](https://github.com/biicode/bii-server/blob/d2d7f2f0e38ff5ffdf1918ddeb33d1f4b1b530b1/model/epoch/utc_datetime.py)
- [ ] stops
- [x] \_\_eq\_\_
- [x] \_\_init\_\_
- [ ] parse
- [ ] end\_of\_day()
- [x] naive

#### alfred-datetime-format-converter
- [ ] stops
- [ ] \_\_eq\_\_
- [x] \_\_init\_\_
    -  [parse_query_value](https://github.com/mwaterfall/alfred-datetime-format-converter/blob/02ffc84ff8e971840d3a3134e4b2682484c4f489/workflow/process.py) returns a delorean object. We should follow this back for eqm end of day, and naive.
- [x] parse
    - [parse_query_value](https://github.com/mwaterfall/alfred-datetime-format-converter/blob/02ffc84ff8e971840d3a3134e4b2682484c4f489/workflow/process.py) 
- [ ] end\_of\_day()
- [ ] naive

#### courtside
- [ ] stops
- [ ] \_\_eq\_\_
- [ ] \_\_init\_\_
- [x] parse
    - [localize_datetime](https://github.com/myusuf3/courtside/blob/6d427391c543cc602ae2d92e1aa61ea15721645b/courtside/game/templatetags/time_tags.py) 
- [ ] end\_of\_day()
- [x] naive
    - [CleanGamesTask](https://github.com/myusuf3/courtside/blob/6d427391c543cc602ae2d92e1aa61ea15721645b/courtside/register/tasks.py) 


## Commits
Every sub-point is a description of a semantic change 
to one library that preserves interfaces. Every sub-sub-point 
is the name of a (unchanged) client that calls this changed 
library

- ``upping version``
- ``adding pypy and pypy3``
- ``fixing tests and adding new build versions``
- ``adding 3.4 support and version bump``
- ``rule parameters weren't being passed, so stops function wasn't working properly.``
- [``Merge pull request #49 from xgilest/master``](https://github.com/myusuf3/delorean/commit/344ed62d440c2189c33a49c7fc7bd5fb32fea8e3)
    - delorean/interface.py/stops
        - No clients inside of project
- ``bumping version``
- ``adding comma``
- ``Small test to check stops bug was resolved by my previous commit, not all rrule functionality is checked, though``
- ``Merge pull request #50 from xgilest/master``
- ``Point README to the docs instead of "below"``
- ``Merge pull request #55 from kermit666/patch-1``
- ``Implemented timedelta arithmetic.``
- ``Added documentation for timezone arithmetic.``
- ``Finished up date arithmetic to better mirror datetime's functionality. Added test_suite to setup.py for test running.``
- ``Updated documentation``
- ``Merge pull request #56 from josefdlange/master``
- ``testing naive truncating to the minute``
- ``updating pytz``
- ``updating pytz``
- ``fixing the dependencies``
- ``fixing requirements``
- ``bumping version``
- ``Added title heading to timedelta arithmetic section.``
- ``Merge pull request #58 from josefdlange/master``
- ``Move to use pip-tools to manaage requirements``
- ``Remove extra 'precedence' in quickstart docs``
- ``Removes weird link generated by Sphinx``
- ``Delorean objects are equal if they are UTC equal``
- ``Merge pull request #59 from mlew/52``
- ``Merge pull request #60 from mlew/51``
- ``Merge pull request #62 from mlew/61``
- ``adding functionality for start_of_day, and end_of_day``
- ``adding tests``
- [``Merge branch 'master' into pip-tools``](https://github.com/myusuf3/delorean/commit/c5b23b96093544bdd3f84f2a9f84efa3bff9fac6)
    - Delorean.\_\_eq\_\_ changed to check that epochs are the same.
        - Hard to find clients for this.
- ``Added documentation for Delorean.__eq__``
- ``end_of_day should return 11pm, not 11am``
- ``Merge pull request #67 from mlew/66``
- ``Merge pull request #63 from mlew/61``
- ``Update __repr__ return value``
- ``Merge pull request #69 from mlew/64``
- ``Migrate Delorean to work with FixedOffset timezones``
- ``Cleanup code example in README.md``
- ``Add CHANGES.md``
- ``update requirements.txt``
- ``Bump version to 0.6.0``
- ``Remove unused utc variables``
- [``Delorean.parse() understands dateutil.tz.tzlocal``](https://github.com/myusuf3/delorean/commit/679596a0ffe7ea72e605cc6b2bf765c036f588b6)
    - dates.py/Delorean.\_\_init\_\_ added self.\_tzinfo = self.\_dt.tzinfo deeply nested in conditionals
        - No clients inside of project
    - delorean/interface.py\parse changes conditionals for when datetime object is offset and when it is local
        - No clients inside of project
- ``Add tzlocal as a dependency``
- ``Update documentation on Delorean properties``
- ``Update a bunch of the documentation``
- ``Update CHANGES.md``
- ``Merge pull request #71 from mlew/70``
- ``Documentation update``
- [``Merge branch 'master' into pip-tools``](https://github.com/myusuf3/delorean/commit/081c758045d6c3b56583d1f139d4bae4c7b9687f)
    - delorean/dates.py/end\_of\_day() (initially incorrectly used 12 hour clock)
        - No clients inside of project
- ``Merge branch 'pip-tools' into 40``
- ``Fix delorean.now() to return a local Delorean``
- ``Move a bunch of Delorean class methods to properties``
- ``Update requirements``
- ``Add sphinx to dev-requirements``
- ``Update docs target in Makefile``
- [``Adding doctests``](https://github.com/myusuf3/delorean/commit/4755906335c825a32db8b65e971f3d3a8b966a8d)
    - delorean/dates.py/naive
        - No clients inside of project
- ``Add more documentation``
- ``Update dev-requirements``
- ``Last bit of new documentation for 0.6.0``
- ``Add humanize method to Delorean class``
- ``Add babel support``
- ``Add an overriding timezone parameter to delorean.parse``
- ``Update setup.py``
- ``README cleanup``
- ``fix for travis.ci``
- ``setup.py fix``
- ``Fix unit tests for case where get_localzone is in UTC``
- ``Python2.6 compatability``
- ``Some last minute cleanup``
- ``Updates to Changes.rst for 0.6.0 release.``
- ``Merge pull request #73 from mlew/0.6.0``
- ``Update requirements files``
- ``Update dependencies in setup.py``
- ``Call out breaking changes in the documentation``
- ``Fix quickstart docs``
- ``Merge pull request #78 from matiskay/fix-documentation``
- ``Added replace method on Delorean object``
- ``Added docs for the replace method``
- ``Updated tests``
- ``Added a few asserts on datetime``
- ``Add PyCharm dir to gitignore.``
- ``Use `naive` and `midnight` as properties in documentation. Closes myusuf3/delorean#88.``
- ``Delete empty philosophy.rst``
- ``Merge pull request #89 from ParthGandhi/fix-quickstart-docs``
- ``Include tests in release source tarball``
- ``Merge pull request #90 from EdwardBetts/patch-1``
- ``adding test for dayfirst False``
- ``Merge branch 'master' of github.com:myusuf3/delorean``
- ``Merge pull request #81 from masnun/master``
- ``adding python 3.5``
- ``Merge branch 'master' of github.com:myusuf3/delorean``
- ``Add most recent Python versions in Travis CI``
- ``Remove nightly from .travis.yml file``
- ``Merge pull request #98 from SylvainDe/master``

## Notes
- ``Added a few asserts on datetime`` adds asserts to the test\_replace function. This is technically a semantic change to a single function that doesn't modify signatures. But it will have no clients other than the test harness. Let's ignore tests.
-  ``Add an overriding timezone parameter to delorean.parse`` delorean/interface.py/parse changes signature but by adding an argument with a default parameter. It's not a very interesting change anyway.
-  ``Remove unused utc variables`` in a test. 
-  [``Migrate Delorean to work with FixedOffset timezones``](https://github.com/myusuf3/delorean/commit/afac86a678728be24b7dbf1670e568b2c246b563). A lot of changes that would fit criteria if taken individually. Really this is a big interface change.
- ``Merge pull request #69 from mlew/64`` Update \_\_repr\_\_ return value. Technically this fits. But it's a waste of time to model/analyze.
- [``Fix delorean.now() to return a local Delorean``](https://github.com/myusuf3/delorean/commit/976e21761f404faf7063b85bf522b18dbf29fbf3)
    - delorean/interface.py/now (returns Delorean object for at local timezone of caller rather than UTC)
        - Difficult to model, not CSEC, no clients inside of project
- ``rule parameters weren't being passed, so stops function wasn't working properly.``
     - same as ``Merge pull request #49 from xgilest/master``
- [``Delorean objects are equal if they are UTC equal``](https://github.com/myusuf3/delorean/commit/081c758045d6c3b56583d1f139d4bae4c7b9687f)
    - same as ``Merge branch 'master' into pip-tools``
- ``Merge pull request #62 from mlew/61``
    - same as ``Merge branch 'master' into pip-tools``
- ``end_of_day should return 11pm, not 11am``
    - same as ``Merge branch 'master' into pip-tools`` 
- ``Merge pull request #67 from mlew/66``
    - same as ``Merge branch 'master' into pip-tools`` 