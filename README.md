This is an example for how this proposed fix can address the issue of omitted
files in the report if they have no tests:
https://github.com/bazelbuild/rules_python/pull/2607

## Setup

```bash
git clone https://github.com/burnzz/rules_python
cd rules_python
git checkout coveragepy-source
git clone https://github.com/BurnzZ/bazel-python-omitted-coverage examples/
cd examples/bazel-python-omitted-coverage
```

Note that this repo already has this line in `MODULE.bazel`, which utilizes the
fix in the `coveragepy-source` branch of `rules_python`.

```python
local_path_override(
    module_name = "rules_python",
    path = "../..",
)
```

We can then confirm the fix via:

```bash
bazel coverage --combined_report=lcov :test --nocache_test_results --test_output=all
lcov --list "$(bazel info output_path)/_coverage/_coverage_report.dat"
```

The output should then show that `no_tests.py` is included in the report with
0 coverage 🎉 :

```
                  |Lines       |Functions
Filename          |Rate     Num|Rate    Num
===========================================
[src/]
has_tests.py      | 100%      3|    -     0
no_tests.py       | 0.0%      2|    -     0
===========================================
            Total:|60.0%      5|    -     0
Message summary:
  no messages were reported
```
