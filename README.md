<h1 align="center">
  <br>
  <a href="https://github.com/vald-phoenix/pylint-errors"><img src="media/logo.png" width="200px" height="auto" alt="plerr"></a>
  <br>
</h1>

<h4 align="center">A list of pylint-errors with reasoning and examples of erroneous and correct code.</h4>

<p align="center">
  <a href="https://github.com/vald-phoenix/pylint-errors/blob/master/LICENSE">
    <img src="https://img.shields.io/pypi/l/plerr">
  </a>
  <a href="https://github.com/vald-phoenix/pylint-errors/actions?workflow=CI">
    <img src="https://github.com/vald-phoenix/pylint-errors/workflows/CI/badge.svg">
  </a>
  <a href="https://codecov.io/gh/vald-phoenix/pylint-errors">
    <img src="https://codecov.io/gh/vald-phoenix/pylint-errors/branch/master/graph/badge.svg">
  </a>
  <a href="https://github.com/vald-phoenix/pylint-errors">
      <img src="https://img.shields.io/pypi/pyversions/plerr">
  </a>
  <a href="https://pypi.org/project/plerr/">
      <img src="https://img.shields.io/pypi/v/plerr">
  </a>
  <a href="https://pypi.org/project/plerr/">
      <img src="https://img.shields.io/pypi/wheel/plerr">
  </a>
</p>

![Example](media/example.svg)

## Table of contents

- [CLI usage](#cli-usage)
  - [Stable release](#stable-release)
  - [Dev builds](#dev-builds)
- [List of errors](#list-of-errors)

## CLI usage

It's not required to install CLI util as long as you can navigate list of
errors [here](#list-of-errors) or on this
[web-site](https://vald-phoenix.github.io/pylint-errors/)
but you may want to do so.  


### Stable release

You can install a stable release simply by such commands:

```console
$ python3 -m pip install plerr
$ plerr r1710
```

For [pipx](https://github.com/pipxproject/pipx):

```console
$ python3 -m pip install pipx # if not yet installed pipx
$ python3 -m pipx ensurepath # ensure directory where pipx stores apps is on PATH
$ pipx install plerr
$ plerr r1710
```

### Dev builds

In order to use development `plerr` builds you need to invoke the following commands:

```console
$ git clone https://github.com/vald-phoenix/pylint-errors.git
$ sudo apt update && sudo apt install -y python3-pip # if not yet installed
$ cd pylint-errors
$ python3 setup.py test
$ python3 setup.py install --user
$ python3 -m plerr r1710
```

[pipx](https://github.com/pipxproject/pipx) users may install the library by
such commands:

```console
$ git clone https://github.com/vald-phoenix/pylint-errors.git
$ sudo apt install -y make python3-pip python3-venv # if not yet installed
$ cd pylint-errors
$ python3 -m pip install pipx wheel # install a package to build a wheel and pipx
$ python3 -m pipx ensurepath # ensure directory where pipx stores apps is on PATH
$ python3 setup.py test # run tests
$ make clean
$ python3 setup.py bdist_wheel # build a binary wheel
$ pipx install dist/* # install a binary wheel by pipx
$ plerr r1710
```

In order to get the latest updates just `git pull origin master` and invoke a
command in the root of the project (`sudo apt install make` if not yet 
installed) `make rai` to install to Python 3 user space site packages or
`make raip` for pipx.

## List of errors

Error codes with **[+]** mean they've got examples of bad and good code.
Rationalisation provided for all entries.

### Async Checker Messages

- [E1700 (yield-inside-async-function)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/async/E1700) **[+]**
- [E1701 (not-async-context-manager)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/async/E1701) **[+]**

### Basic Checker Messages

- [C0102 (blacklisted-name)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/C0102) **[+]**
- [C0103 (invalid-name)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/C0103) **[+]**
- [C0112 (empty-docstring)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/C0112) **[+]**
- [C0114 (missing-module-docstring)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/C0114) **[+]**
- [C0115 (missing-class-docstring)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/C0115) **[+]**
- [C0116 (missing-function-docstring)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/C0116) **[+]**
- [C0121 (singleton-comparison)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/C0121) **[+]**
- [C0122 (misplaced-comparison-constant)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/C0122) **[+]**
- [C0123 (unidiomatic-typecheck)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/C0123) **[+]**
- [E0100 (init-is-generator)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0100) **[+]**
- [E0101 (return-in-init)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0101) **[+]**
- [E0102 (function-redefined)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0102) **[+]**
- [E0103 (not-in-loop)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0103) **[+]**
- [E0104 (return-outside-function)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0104) **[+]**
- [E0105 (yield-outside-function)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0105) **[+]**
- [E0106 (return-arg-in-generator)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0106)
- [E0107 (nonexistent-operator)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0107) **[+]**
- [E0108 (duplicate-argument-name)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0108) **[+]**
- [E0110 (abstract-class-instantiated)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0110) **[+]**
- [E0111 (bad-reversed-sequence)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0111) **[+]**
- [E0112 (too-many-star-expressions)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0112) **[+]**
- [E0113 (invalid-star-assignment-target)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0113) **[+]**
- [E0114 (star-needs-assignment-target)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0114) **[+]**
- [E0115 (nonlocal-and-global)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0115) **[+]**
- [E0116 (continue-in-finally)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0116) **[+]**
- [E0117 (nonlocal-without-binding)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0117) **[+]**
- [E0118 (used-prior-global-declaration)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0118) **[+]**
- [E0119 (misplaced-format-function)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/E0119) **[+]**
- [R0123 (literal-comparison)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/R0123) **[+]**
- [R0124 (comparison-with-itself)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/R0124) **[+]**
- [W0101 (unreachable)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0101) **[+]**
- [W0102 (dangerous-default-value)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0102) **[+]**
- [W0104 (pointless-statement)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0104) **[+]**
- [W0105 (pointless-string-statement)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0105) **[+]**
- [W0106 (expression-not-assigned)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0106) **[+]**
- [W0107 (unnecessary-pass)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0107) **[+]**
- [W0108 (unnecessary-lambda)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0108) **[+]**
- [W0109 (duplicate-key)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0109) **[+]**
- [W0111 (assign-to-new-keyword)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0111) **[+]**
- [W0120 (useless-else-on-loop)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0120) **[+]**
- [W0122 (exec-used)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0122) **[+]**
- [W0123 (eval-used)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0123) **[+]**
- [W0124 (confusing-with-statement)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0124) **[+]**
- [W0125 (using-constant-test)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0125)
- [W0126 (missing-parentheses-for-call-in-test)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0126)
- [W0127 (self-assigning-variable)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0127) **[+]**
- [W0128 (redeclared-assigned-name)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0128)
- [W0143 (comparison-with-callable)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0143) **[+]**
- [W0150 (lost-exception)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0150) **[+]**
- [W0199 (assert-on-tuple)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/W0199) **[+]**

### Broad Try Clause Checker Messages

- [W0717 (too-many-try-statements)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/broad-try-clause/W0717)

### Classes Checker Messages

- [C0202 (bad-classmethod-argument)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/C0202) **[+]**
- [C0203 (bad-mcs-method-argument)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/C0203) **[+]**
- [C0204 (bad-mcs-classmethod-argument)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/C0204) **[+]**
- [C0205 (single-string-used-for-slots)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/C0205) **[+]**
- [E0202 (method-hidden)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0202) **[+]**
- [E0203 (access-member-before-definition)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0203) **[+]**
- [E0211 (no-method-argument)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0211) **[+]**
- [E0213 (no-self-argument)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0213) **[+]**
- [E0236 (invalid-slots-object)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0236) **[+]**
- [E0237 (assigning-non-slot)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0237) **[+]**
- [E0238 (invalid-slots)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0238) **[+]**
- [E0239 (inherit-non-class)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0239) **[+]**
- [E0240 (inconsistent-mro)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0240) **[+]**
- [E0241 (duplicate-bases)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0241) **[+]**
- [E0242 (class-variable-slots-conflict)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0242) **[+]**
- [E0301 (non-iterator-returned)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0301) **[+]**
- [E0302 (unexpected-special-method-signature)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0302) **[+]**
- [E0303 (invalid-length-returned)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/E0303) **[+]**
- [F0202 (method-check-failed)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/F0202)
- [R0201 (no-self-use)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/R0201)  **[+]**
- [R0202 (no-classmethod-decorator)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/R0202) **[+]**
- [R0203 (no-staticmethod-decorator)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/R0203) **[+]**
- [R0205 (useless-object-inheritance)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/R0205) **[+]**
- [R0206 (property-with-parameters)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/R0206) **[+]**
- [W0201 (attribute-defined-outside-init)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/W0201) **[+]**
- [W0211 (bad-staticmethod-argument)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/W0211) **[+]**
- [W0212 (protected-access)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/W0212) **[+]**
- [W0221 (arguments-differ)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/W0221) **[+]**
- [W0222 (signature-differs)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/W0222)
- [W0223 (abstract-method)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/W0223) **[+]**
- [W0231 (super-init-not-called)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/W0231) **[+]**
- [W0232 (no-init)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/W0232) **[+]**
- [W0233 (non-parent-init-called)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/W0233) **[+]**
- [W0235 (useless-super-delegation)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/W0235) **[+]**
- [W0236 (invalid-overridden-method)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/classes/W0236) **[+]**

### Compare-To-Empty-String Checker Messages

- [C1901 (compare-to-empty-string)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/compare-to-empty-string/C1901) **[+]**

### Compare-To-Zero Checker Messages

- [C2001 (compare-to-zero)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/compare-to-zero/C2001) **[+]**

### Deprecated Builtins Checker Messages

- [W0141 (bad-builtin)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/deprecated-builtins/W0141) **[+]**

### Design Checker Messages

- [R0901 (too-many-ancestors)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/design/R0901) **[+]**
- [R0902 (too-many-instance-attributes)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/design/R0902) **[+]**
- [R0903 (too-few-public-methods)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/design/R0903) **[+]**
- [R0904 (too-many-public-methods)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/design/R0904) **[+]**
- [R0911 (too-many-return-statements)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/design/R0911) **[+]**
- [R0912 (too-many-branches)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/design/R0912) **[+]**
- [R0913 (too-many-arguments)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/design/R0913) **[+]**
- [R0914 (too-many-locals)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/design/R0914) **[+]**
- [R0915 (too-many-statements)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/design/R0915) **[+]**
- [R0916 (too-many-boolean-expressions)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/design/R0916) **[+]**
- [R1260 (too-complex)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/design/R1260) **[+]**

### Docstyle Checker Messages

- [C0198 (bad-docstring-quotes)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/docstyle/C0198) **[+]**
- [C0199 (docstring-first-line-empty)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/docstyle/C0199) **[+]**

### Else If Used Checker Messages

- [R5501 (else-if-used)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/else-if-used/R5501) **[+]**

### Exceptions Checker Messages

- [E0701 (bad-except-order)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/E0701) **[+]**
- [E0702 (raising-bad-type)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/E0702) **[+]**
- [E0703 (bad-exception-context)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/E0703) **[+]**
- [E0704 (misplaced-bare-raise)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/E0704) **[+]**
- [E0710 (raising-non-exception)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/E0710) **[+]**
- [E0711 (notimplemented-raised)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/E0711) **[+]**
- [E0712 (catching-non-exception)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/E0712) **[+]**
- [W0702 (bare-except)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/W0702) **[+]**
- [W0703 (broad-except)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/W0703) **[+]**
- [W0705 (duplicate-except)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/W0705) **[+]**
- [W0706 (try-except-raise)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/W0706) **[+]**
- [W0711 (binary-op-exception)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/W0711) **[+]**
- [W0715 (raising-format-tuple)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/W0715) **[+]**
- [W0716 (wrong-exception-operation)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/exceptions/W0716) **[+]**

### Format Checker Messages

- [C0301 (line-too-long)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/C0301) **[+]**
- [C0302 (too-many-lines)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/C0302)
- [C0303 (trailing-whitespace)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/C0303) **[+]**
- [C0304 (missing-final-newline)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/C0304)
- [C0305 (trailing-newlines)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/C0305)
- [C0321 (multiple-statements)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/C0321) **[+]**
- [C0325 (superfluous-parens)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/C0325) **[+]**
- [C0326 (bad-whitespace)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/C0326) **[+]**
- [C0327 (mixed-line-endings)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/C0327)
- [C0328 (unexpected-line-ending-format)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/C0328)
- [C0330 (bad-continuation)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/C0330)
- [W0301 (unnecessary-semicolon)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/W0301) **[+]**
- [W0311 (bad-indentation)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/W0311) **[+]**
- [W0312 (mixed-indentation)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/W0312)

### Imports Checker Messages

- [C0410 (multiple-imports)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/C0410) **[+]**
- [C0411 (wrong-import-order)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/C0411) **[+]**
- [C0412 (ungrouped-imports)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/C0412) **[+]**
- [C0413 (wrong-import-position)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/C0413) **[+]**
- [C0414 (useless-import-alias)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/C0414) **[+]**
- [C0415 (import-outside-toplevel)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/C0415) **[+]**
- [E0401 (import-error)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/E0401) **[+]**
- [E0402 (relative-beyond-top-level)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/E0402) **[+]**
- [R0401 (cyclic-import)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/R0401) **[+]**
- [W0401 (wildcard-import)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/W0401) **[+]**
- [W0402 (deprecated-module)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/W0402) **[+]**
- [W0404 (reimported)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/W0404) **[+]**
- [W0406 (import-self)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/W0406) **[+]**
- [W0407 (preferred-module)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/W0407) **[+]**
- [W0410 (misplaced-future)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/imports/W0410) **[+]**

### Logging Checker Messages

- [E1200 (logging-unsupported-format)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/logging/E1200)
- [E1201 (logging-format-truncated)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/logging/E1201)
- [E1205 (logging-too-many-args)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/logging/E1205)
- [E1206 (logging-too-few-args)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/logging/E1206)
- [W1201 (logging-not-lazy)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/logging/W1201) **[+]**
- [W1202 (logging-format-interpolation)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/logging/W1202) **[+]**

### Miscellaneous Checker Messages

- [I0023 (use-symbolic-message-instead)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/miscellaneous/I0023)
- [W0511 (fixme)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/miscellaneous/W0511) **[+]**

### Multiple Types Checker Messages

- [R0204 (redefined-variable-type)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/multiple-types/R0204)

### Newstyle Checker Messages

- [E1003 (bad-super-call)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/newstyle/E1003) **[+]**

### Overlap-Except Checker Messages

- [W0714 (overlapping-except)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/overlap-except/W0714)

### Parameter Documentation Checker Messages

- [W9005 (multiple-constructor-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9005) **[+]**
- [W9006 (missing-raises-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9006) **[+]**
- [W9008 (redundant-returns-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9008)
- [W9010 (redundant-yields-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9010)
- [W9011 (missing-return-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9011) **[+]**
- [W9012 (missing-return-type-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9012) **[+]**
- [W9013 (missing-yield-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9013)
- [W9014 (missing-yield-type-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9014)
- [W9015 (missing-param-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9015) **[+]**
- [W9016 (missing-type-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9016) **[+]**
- [W9017 (differing-param-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9017) **[+]**
- [W9018 (differing-type-doc)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/parameter-documentation/W9018) **[+]**

### Refactoring Checker Messages

- [C0113 (unneeded-not)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/C0113) **[+]**
- [C0200 (consider-using-enumerate)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/C0200) **[+]**
- [C0201 (consider-iterating-dictionary)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/C0201) **[+]**
- [C1801 (len-as-condition)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/C1801) **[+]**
- [R1701 (consider-merging-isinstance)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1701)
- [R1702 (too-many-nested-blocks)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1702)
- [R1703 (simplifiable-if-statement)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1703) **[+]**
- [R1704 (redefined-argument-from-local)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1704) **[+]**
- [R1705 (no-else-return)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1705) **[+]**
- [R1706 (consider-using-ternary)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1706)
- [R1707 (trailing-comma-tuple)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1707) **[+]**
- [R1708 (stop-iteration-return)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1708) **[+]**
- [R1709 (simplify-boolean-expression)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1709)
- [R1710 (inconsistent-return-statements)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1710) **[+]**
- [R1711 (useless-return)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1711) **[+]**
- [R1712 (consider-swap-variables)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1712) **[+]**
- [R1713 (consider-using-join)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1713) **[+]**
- [R1714 (consider-using-in)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1714) **[+]**
- [R1715 (consider-using-get)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1715)
- [R1716 (chained-comparison)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1716) **[+]**
- [R1717 (consider-using-dict-comprehension)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1717)
- [R1718 (consider-using-set-comprehension)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1718)
- [R1719 (simplifiable-if-expression)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1719) **[+]**
- [R1720 (no-else-raise)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1720) **[+]**
- [R1721 (unnecessary-comprehension)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1721) **[+]**
- [R1722 (consider-using-sys-exit)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1722) **[+]**
- [R1723 (no-else-break)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1723) **[+]**
- [R1724 (no-else-continue)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/refactoring/R1724) **[+]**

### Similarities Checker Messages

- [R0801 (duplicate-code)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/similarities/R0801)

### Spelling Checker Messages

- [C0401 (wrong-spelling-in-comment)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/spelling/C0401)
- [C0402 (wrong-spelling-in-docstring)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/spelling/C0402)
- [C0403 (invalid-characters-in-docstring)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/spelling/C0403)

### Stdlib Checker Messages

- [E1507 (invalid-envvar-value)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/stdlib/E1507) **[+]**
- [W1501 (bad-open-mode)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/stdlib/W1501) **[+]**
- [W1502 (boolean-datetime)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/stdlib/W1502)
- [W1503 (redundant-unittest-assert)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/stdlib/W1503) **[+]**
- [W1505 (deprecated-method)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/stdlib/W1505)
- [W1506 (bad-thread-instantiation)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/stdlib/W1506) **[+]**
- [W1507 (shallow-copy-environ)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/stdlib/W1507) **[+]**
- [W1508 (invalid-envvar-default)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/stdlib/W1508) **[+]**
- [W1509 (subprocess-popen-preexec-fn)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/stdlib/W1509) **[+]**
- [W1510 (subprocess-run-check)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/stdlib/W1510) **[+]**

### String Checker Messages

- [E1300 (bad-format-character)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/E1300) **[+]**
- [E1301 (truncated-format-string)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/E1301)
- [E1302 (mixed-format-string)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/E1302) **[+]**
- [E1303 (format-needs-mapping)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/E1303)
- [E1304 (missing-format-string-key)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/E1304) **[+]**
- [E1305 (too-many-format-args)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/E1305) **[+]**
- [E1306 (too-few-format-args)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/E1306) **[+]**
- [E1307 (bad-string-format-type)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/E1307) **[+]**
- [E1310 (bad-str-strip-call)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/E1310)
- [W1300 (bad-format-string-key)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1300)
- [W1301 (unused-format-string-key)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1301)
- [W1302 (bad-format-string)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1302) **[+]**
- [W1303 (missing-format-argument-key)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1303) **[+]**
- [W1304 (unused-format-string-argument)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1304) **[+]**
- [W1305 (format-combined-specification)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1305) **[+]**
- [W1306 (missing-format-attribute)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1306) **[+]**
- [W1307 (invalid-format-index)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1307) **[+]**
- [W1308 (duplicate-string-formatting-argument)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1308)
- [W1401 (anomalous-backslash-in-string)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1401)
- [W1402 (anomalous-unicode-escape-in-string)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1402) **[+]**
- [W1403 (implicit-str-concat-in-sequence)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/string/W1403)

### Typecheck Checker Messages

- [E1101 (no-member)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1101) **[+]**
- [E1102 (not-callable)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1102) **[+]**
- [E1111 (assignment-from-no-return)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1111) **[+]**
- [E1120 (no-value-for-parameter)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1120) **[+]**
- [E1121 (too-many-function-args)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1121) **[+]**
- [E1123 (unexpected-keyword-arg)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1123) **[+]**
- [E1124 (redundant-keyword-arg)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1124) **[+]**
- [E1125 (missing-kwoa)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1125)
- [E1126 (invalid-sequence-index)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1126) **[+]**
- [E1127 (invalid-slice-index)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1127) **[+]**
- [E1128 (assignment-from-none)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1128) **[+]**
- [E1129 (not-context-manager)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1129) **[+]**
- [E1130 (invalid-unary-operand-type)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1130) **[+]**
- [E1131 (unsupported-binary-operation)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1131) **[+]**
- [E1132 (repeated-keyword)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1132)
- [E1133 (not-an-iterable)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1133) **[+]**
- [E1134 (not-a-mapping)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1134)
- [E1135 (unsupported-membership-test)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1135) **[+]**
- [E1136 (unsubscriptable-object)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1136) **[+]**
- [E1137 (unsupported-assignment-operation)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1137) **[+]**
- [E1138 (unsupported-delete-operation)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1138) **[+]**
- [E1139 (invalid-metaclass)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1139)
- [E1140 (unhashable-dict-key)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1140) **[+]**
- [E1141 (dict-iter-missing-items)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/E1141) **[+]**
- [I1101 (c-extension-no-member)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/I1101)
- [W1113 (keyword-arg-before-vararg)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/W1113) **[+]**
- [W1114 (arguments-out-of-order)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/typecheck/W1114)

### Variables Checker Messages

- [E0601 (used-before-assignment)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/E0601) **[+]**
- [E0602 (undefined-variable)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/E0602)
- [E0603 (undefined-all-variable)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/E0603) **[+]**
- [E0604 (invalid-all-object)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/E0604) **[+]**
- [E0611 (no-name-in-module)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/E0611) **[+]**
- [E0633 (unpacking-non-sequence)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/E0633) **[+]**
- [W0601 (global-variable-undefined)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0601) **[+]**
- [W0602 (global-variable-not-assigned)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0602) **[+]**
- [W0603 (global-statement)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0603) **[+]**
- [W0604 (global-at-module-level)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0604) **[+]**
- [W0611 (unused-import)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0611) **[+]**
- [W0612 (unused-variable)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0612) **[+]**
- [W0613 (unused-argument)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0613) **[+]**
- [W0614 (unused-wildcard-import)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0614) **[+]**
- [W0621 (redefined-outer-name)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0621) **[+]**
- [W0622 (redefined-builtin)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0622) **[+]**
- [W0623 (redefine-in-handler)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0623)
- [W0631 (undefined-loop-variable)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0631) **[+]**
- [W0632 (unbalanced-tuple-unpacking)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0632) **[+]**
- [W0640 (cell-var-from-loop)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0640) **[+]**
- [W0641 (possibly-unused-variable)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0641)
- [W0642 (self-cls-assignment)](https://vald-phoenix.github.io/pylint-errors/plerr/errors/variables/W0642)
