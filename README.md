[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/vald-phoenix/pylint-errors/blob/master/LICENSE)

# pylint-errors

A list of pylint-errors with reasoning and examples of erroneous and
correct code.

## List of errors

Error codes with **[+]** mean they've got examples of bad and good code.
Rationalisation provided for all entries.

### Async Checker Messages

- [E1700 (yield-inside-async-function)](errors/async/E1700.md)
- [E1701 (not-async-context-manager)](errors/async/E1701.md)

### Basic Checker Messages

- [C0102 (blacklisted-name)](errors/basic/C0102.md)
- [C0103 (invalid-name)](errors/basic/C0103.md)
- [C0112 (empty-docstring)](errors/basic/C0112.md)
- [C0114 (missing-module-docstring)](errors/basic/C0114.md)
- [C0115 (missing-class-docstring)](errors/basic/C0115.md)
- [C0116 (missing-function-docstring)](errors/basic/C0116.md) **[+]**
- [C0121 (singleton-comparison)](errors/basic/C0121.md)
- [C0122 (misplaced-comparison-constant)](errors/basic/C0122.md)
- [C0123 (unidiomatic-typecheck)](errors/basic/C0123.md)
- [E0100 (init-is-generator)](errors/basic/E0100.md)
- [E0101 (return-in-init)](errors/basic/E0101.md)
- [E0102 (function-redefined)](errors/basic/E0102.md)
- [E0103 (not-in-loop)](errors/basic/E0103.md)
- [E0104 (return-outside-function)](errors/basic/E0104.md)
- [E0105 (yield-outside-function)](errors/basic/E0105.md)
- [E0106 (return-arg-in-generator)](errors/basic/E0106.md)
- [E0107 (nonexistent-operator)](errors/basic/E0107.md)
- [E0108 (duplicate-argument-name)](errors/basic/E0108.md)
- [E0110 (abstract-class-instantiated)](errors/basic/E0110.md)
- [E0111 (bad-reversed-sequence)](errors/basic/E0111.md)
- [E0112 (too-many-star-expressions)](errors/basic/E0112.md)
- [E0113 (invalid-star-assignment-target)](errors/basic/E0113.md)
- [E0114 (star-needs-assignment-target)](errors/basic/E0114.md)
- [E0115 (nonlocal-and-global)](errors/basic/E0115.md)
- [E0116 (continue-in-finally)](errors/basic/E0116.md)
- [E0117 (nonlocal-without-binding)](errors/basic/E0117.md)
- [E0118 (used-prior-global-declaration)](errors/basic/E0118.md)
- [E0119 (misplaced-format-function)](errors/basic/E0119.md)
- [R0123 (literal-comparison)](errors/basic/R0123.md)
- [R0124 (comparison-with-itself)](errors/basic/R0124.md)
- [W0101 (unreachable)](errors/basic/W0101.md)
- [W0102 (dangerous-default-value)](errors/basic/W0102.md)
- [W0104 (pointless-statement)](errors/basic/W0104.md)
- [W0105 (pointless-string-statement)](errors/basic/W0105.md)
- [W0106 (expression-not-assigned)](errors/basic/W0106.md)
- [W0107 (unnecessary-pass)](errors/basic/W0107.md)
- [W0108 (unnecessary-lambda)](errors/basic/W0108.md)
- [W0109 (duplicate-key)](errors/basic/W0109.md)
- [W0111 (assign-to-new-keyword)](errors/basic/W0111.md)
- [W0120 (useless-else-on-loop)](errors/basic/W0120.md)
- [W0122 (exec-used)](errors/basic/W0122.md)
- [W0123 (eval-used)](errors/basic/W0123.md)
- [W0124 (confusing-with-statement)](errors/basic/W0124.md)
- [W0125 (using-constant-test)](errors/basic/W0125.md)
- [W0126 (missing-parentheses-for-call-in-test)](errors/basic/W0126.md)
- [W0127 (self-assigning-variable)](errors/basic/W0127.md)
- [W0128 (redeclared-assigned-name)](errors/basic/W0128.md)
- [W0143 (comparison-with-callable)](errors/basic/W0143.md)
- [W0150 (lost-exception)](errors/basic/W0150.md)
- [W0199 (assert-on-tuple)](errors/basic/W0199.md)

### Broad Try Clause Checker Messages

- [W0717 (too-many-try-statements)](errors/broad-try-clause/W0717.md)

### Classes Checker Messages

- [C0202 (bad-classmethod-argument)](errors/classes/C0202.md)
- [C0203 (bad-mcs-method-argument)](errors/classes/C0203.md)
- [C0204 (bad-mcs-classmethod-argument)](errors/classes/C0204.md)
- [C0205 (single-string-used-for-slots)](errors/classes/C0205.md)
- [E0202 (method-hidden)](errors/classes/E0202.md)
- [E0203 (access-member-before-definition)](errors/classes/E0203.md)
- [E0211 (no-method-argument)](errors/classes/E0211.md)
- [E0213 (no-self-argument)](errors/classes/E0213.md)
- [E0236 (invalid-slots-object)](errors/classes/E0236.md)
- [E0237 (assigning-non-slot)](errors/classes/E0237.md)
- [E0238 (invalid-slots)](errors/classes/E0238.md)
- [E0239 (inherit-non-class)](errors/classes/E0239.md)
- [E0240 (inconsistent-mro)](errors/classes/E0240.md)
- [E0241 (duplicate-bases)](errors/classes/E0241.md)
- [E0242 (class-variable-slots-conflict)](errors/classes/E0242.md)
- [E0301 (non-iterator-returned)](errors/classes/E0301.md)
- [E0302 (unexpected-special-method-signature)](errors/classes/E0302.md)
- [E0303 (invalid-length-returned)](errors/classes/E0303.md)
- [F0202 (method-check-failed)](errors/classes/F0202.md)
- [R0201 (no-self-use)](errors/classes/R0201.md)
- [R0202 (no-classmethod-decorator)](errors/classes/R0202.md)
- [R0203 (no-staticmethod-decorator)](errors/classes/R0203.md)
- [R0205 (useless-object-inheritance)](errors/classes/R0205.md) **[+]**
- [R0206 (property-with-parameters)](errors/classes/R0206.md)
- [W0201 (attribute-defined-outside-init)](errors/classes/W0201.md)
- [W0211 (bad-staticmethod-argument)](errors/classes/W0211.md)
- [W0212 (protected-access)](errors/classes/W0212.md)
- [W0221 (arguments-differ)](errors/classes/W0221.md)
- [W0222 (signature-differs)](errors/classes/W0222.md)
- [W0223 (abstract-method)](errors/classes/W0223.md)
- [W0231 (super-init-not-called)](errors/classes/W0231.md)
- [W0232 (no-init)](errors/classes/W0232.md)
- [W0233 (non-parent-init-called)](errors/classes/W0233.md)
- [W0235 (useless-super-delegation)](errors/classes/W0235.md)
- [W0236 (invalid-overridden-method)](errors/classes/W0236.md)

### Compare-To-Empty-String Checker Messages

- [C1901 (compare-to-empty-string)](errors/compare-to-empty-string/C1901.md)

### Compare-To-Zero Checker Messages

- [C2001 (compare-to-zero)](errors/compare-to-zero/C2001.md)

### Deprecated Builtins Checker Messages

- [W0141 (bad-builtin)](errors/deprecated-builtins/W0141.md)

### Design Checker Messages

- [R0901 (too-many-ancestors)](errors/design/R0901.md)
- [R0902 (too-many-instance-attributes)](errors/design/R0902.md)
- [R0903 (too-few-public-methods)](errors/design/R0903.md) **[+]**
- [R0904 (too-many-public-methods)](errors/design/R0904.md)
- [R0911 (too-many-return-statements)](errors/design/R0911.md)
- [R0912 (too-many-branches)](errors/design/R0912.md)
- [R0913 (too-many-arguments)](errors/design/R0913.md)
- [R0914 (too-many-locals)](errors/design/R0914.md)
- [R0915 (too-many-statements)](errors/design/R0915.md)
- [R0916 (too-many-boolean-expressions)](errors/design/R0916.md)
- [R1260 (too-complex)](errors/design/R1260.md)

### Docstyle Checker Messages

- [C0198 (bad-docstring-quotes)](errors/docstyle/C0198.md)
- [C0199 (docstring-first-line-empty)](errors/docstyle/C0199.md)

### Else If Used Checker Messages

- [R5501 (else-if-used)](errors/else-if-used/R5501.md)

### Exceptions Checker Messages

- [E0701 (bad-except-order)](errors/exceptions/E0701.md)
- [E0702 (raising-bad-type)](errors/exceptions/E0702.md)
- [E0703 (bad-exception-context)](errors/exceptions/E0703.md)
- [E0704 (misplaced-bare-raise)](errors/exceptions/E0704.md)
- [E0710 (raising-non-exception)](errors/exceptions/E0710.md)
- [E0711 (notimplemented-raised)](errors/exceptions/E0711.md)
- [E0712 (catching-non-exception)](errors/exceptions/E0712.md)
- [W0702 (bare-except)](errors/exceptions/W0702.md)
- [W0703 (broad-except)](errors/exceptions/W0703.md)
- [W0705 (duplicate-except)](errors/exceptions/W0705.md)
- [W0706 (try-except-raise)](errors/exceptions/W0706.md)
- [W0711 (binary-op-exception)](errors/exceptions/W0711.md)
- [W0715 (raising-format-tuple)](errors/exceptions/W0715.md)
- [W0716 (wrong-exception-operation)](errors/exceptions/W0716.md)

### Format Checker Messages

- [C0301 (line-too-long)](errors/format/C0301.md)
- [C0302 (too-many-lines)](errors/format/C0302.md)
- [C0303 (trailing-whitespace)](errors/format/C0303.md)
- [C0304 (missing-final-newline)](errors/format/C0304.md)
- [C0305 (trailing-newlines)](errors/format/C0305.md)
- [C0321 (multiple-statements)](errors/format/C0321.md)
- [C0325 (superfluous-parens)](errors/format/C0325.md)
- [C0326 (bad-whitespace)](errors/format/C0326.md)
- [C0327 (mixed-line-endings)](errors/format/C0327.md)
- [C0328 (unexpected-line-ending-format)](errors/format/C0328.md)
- [C0330 (bad-continuation)](errors/format/C0330.md)
- [W0301 (unnecessary-semicolon)](errors/format/W0301.md)
- [W0311 (bad-indentation)](errors/format/W0311.md)
- [W0312 (mixed-indentation)](errors/format/W0312.md)

### Imports Checker Messages

- [C0410 (multiple-imports)](errors/imports/C0410.md)
- [C0411 (wrong-import-order)](errors/imports/C0411.md)
- [C0412 (ungrouped-imports)](errors/imports/C0412.md)
- [C0413 (wrong-import-position)](errors/imports/C0413.md)
- [C0414 (useless-import-alias)](errors/imports/C0414.md)
- [C0415 (import-outside-toplevel)](errors/imports/C0415.md)
- [E0401 (import-error)](errors/imports/E0401.md)
- [E0402 (relative-beyond-top-level)](errors/imports/E0402.md)
- [R0401 (cyclic-import)](errors/imports/R0401.md)
- [W0401 (wildcard-import)](errors/imports/W0401.md)
- [W0402 (deprecated-module)](errors/imports/W0402.md)
- [W0404 (reimported)](errors/imports/W0404.md)
- [W0406 (import-self)](errors/imports/W0406.md)
- [W0407 (preferred-module)](errors/imports/W0407.md)
- [W0410 (misplaced-future)](errors/imports/W0410.md)

### Logging Checker Messages

- [E1200 (logging-unsupported-format)](errors/logging/E1200.md)
- [E1201 (logging-format-truncated)](errors/logging/E1201.md)
- [E1205 (logging-too-many-args)](errors/logging/E1205.md)
- [E1206 (logging-too-few-args)](errors/logging/E1206.md)
- [W1201 (logging-not-lazy)](errors/logging/W1201.md)
- [W1202 (logging-format-interpolation)](errors/logging/W1202.md)

### Miscellaneous Checker Messages

- [I0023 (use-symbolic-message-instead)](errors/miscellaneous/I0023.md)
- [W0511 (fixme)](errors/miscellaneous/W0511.md)

### Multiple Types Checker Messages

- [R0204 (redefined-variable-type)](errors/multiple-types/R0204.md)

### Newstyle Checker Messages

- [E1003 (bad-super-call)](errors/newstyle/E1003.md)

### Overlap-Except Checker Messages

- [W0714 (overlapping-except)](errors/overlap-except/W0714.md)

### Parameter Documentation Checker Messages

- [W9005 (multiple-constructor-doc)](errors/parameter-documentation/W9005.md)
- [W9006 (missing-raises-doc)](errors/parameter-documentation/W9006.md)
- [W9008 (redundant-returns-doc)](errors/parameter-documentation/W9008.md)
- [W9010 (redundant-yields-doc)](errors/parameter-documentation/W9010.md)
- [W9011 (missing-return-doc)](errors/parameter-documentation/W9011.md)
- [W9012 (missing-return-type-doc)](errors/parameter-documentation/W9012.md)
- [W9013 (missing-yield-doc)](errors/parameter-documentation/W9013.md)
- [W9014 (missing-yield-type-doc)](errors/parameter-documentation/W9014.md)
- [W9015 (missing-param-doc)](errors/parameter-documentation/W9015.md)
- [W9016 (missing-type-doc)](errors/parameter-documentation/W9016.md)
- [W9017 (differing-param-doc)](errors/parameter-documentation/W9017.md)
- [W9018 (differing-type-doc)](errors/parameter-documentation/W9018.md)

### Python3 Checker Messages

- [E1601 (print-statement)](errors/python3/E1601.md)
- [E1602 (parameter-unpacking)](errors/python3/E1602.md)
- [E1603 (unpacking-in-except)](errors/python3/E1603.md)
- [E1604 (old-raise-syntax)](errors/python3/E1604.md)
- [E1605 (backtick)](errors/python3/E1605.md)
- [E1606 (long-suffix)](errors/python3/E1606.md)
- [E1607 (old-ne-operator)](errors/python3/E1607.md)
- [E1608 (old-octal-literal)](errors/python3/E1608.md)
- [E1609 (import-star-module-level)](errors/python3/E1609.md)
- [E1610 (non-ascii-bytes-literal)](errors/python3/E1610.md)
- [W1601 (apply-builtin)](errors/python3/W1601.md)
- [W1602 (basestring-builtin)](errors/python3/W1602.md)
- [W1603 (buffer-builtin)](errors/python3/W1603.md)
- [W1604 (cmp-builtin)](errors/python3/W1604.md)
- [W1605 (coerce-builtin)](errors/python3/W1605.md)
- [W1606 (execfile-builtin)](errors/python3/W1606.md)
- [W1607 (file-builtin)](errors/python3/W1607.md)
- [W1608 (long-builtin)](errors/python3/W1608.md)
- [W1610 (reduce-builtin)](errors/python3/W1610.md)
- [W1611 (standarderror-builtin)](errors/python3/W1611.md)
- [W1612 (unicode-builtin)](errors/python3/W1612.md)
- [W1613 (xrange-builtin)](errors/python3/W1613.md)
- [W1614 (coerce-method)](errors/python3/W1614.md)
- [W1615 (delslice-method)](errors/python3/W1615.md)
- [W1616 (getslice-method)](errors/python3/W1616.md)
- [W1617 (setslice-method)](errors/python3/W1617.md)
- [W1618 (no-absolute-import)](errors/python3/W1618.md)
- [W1619 (old-division)](errors/python3/W1619.md)
- [W1620 (dict-iter-method)](errors/python3/W1620.md)
- [W1621 (dict-view-method)](errors/python3/W1621.md)
- [W1622 (next-method-called)](errors/python3/W1622.md)
- [W1623 (metaclass-assignment)](errors/python3/W1623.md)
- [W1624 (indexing-exception)](errors/python3/W1624.md)
- [W1625 (raising-string)](errors/python3/W1625.md)
- [W1626 (reload-builtin)](errors/python3/W1626.md)
- [W1627 (oct-method)](errors/python3/W1627.md)
- [W1628 (hex-method)](errors/python3/W1628.md)
- [W1629 (nonzero-method)](errors/python3/W1629.md)
- [W1630 (cmp-method)](errors/python3/W1630.md)
- [W1632 (input-builtin)](errors/python3/W1632.md)
- [W1633 (round-builtin)](errors/python3/W1633.md)
- [W1634 (intern-builtin)](errors/python3/W1634.md)
- [W1635 (unichr-builtin)](errors/python3/W1635.md)
- [W1636 (map-builtin-not-iterating)](errors/python3/W1636.md)
- [W1637 (zip-builtin-not-iterating)](errors/python3/W1637.md)
- [W1638 (range-builtin-not-iterating)](errors/python3/W1638.md)
- [W1639 (filter-builtin-not-iterating)](errors/python3/W1639.md)
- [W1640 (using-cmp-argument)](errors/python3/W1640.md)
- [W1641 (eq-without-hash)](errors/python3/W1641.md)
- [W1642 (div-method)](errors/python3/W1642.md)
- [W1643 (idiv-method)](errors/python3/W1643.md)
- [W1644 (rdiv-method)](errors/python3/W1644.md)
- [W1645 (exception-message-attribute)](errors/python3/W1645.md)
- [W1646 (invalid-str-codec)](errors/python3/W1646.md)
- [W1647 (sys-max-int)](errors/python3/W1647.md)
- [W1649 (deprecated-string-function)](errors/python3/W1649.md)
- [W1650 (deprecated-str-translate-call)](errors/python3/W1650.md)
- [W1651 (deprecated-itertools-function)](errors/python3/W1651.md)
- [W1652 (deprecated-types-field)](errors/python3/W1652.md)
- [W1653 (next-method-defined)](errors/python3/W1653.md)
- [W1654 (dict-items-not-iterating)](errors/python3/W1654.md)
- [W1655 (dict-keys-not-iterating)](errors/python3/W1655.md)
- [W1656 (dict-values-not-iterating)](errors/python3/W1656.md)
- [W1657 (deprecated-operator-function)](errors/python3/W1657.md)
- [W1658 (deprecated-urllib-function)](errors/python3/W1658.md)
- [W1659 (xreadlines-attribute)](errors/python3/W1659.md)
- [W1660 (deprecated-sys-function)](errors/python3/W1660.md)
- [W1661 (exception-escape)](errors/python3/W1661.md)
- [W1662 (comprehension-escape)](errors/python3/W1662.md)

### Refactoring Checker Messages

- [C0113 (unneeded-not)](errors/refactoring/C0113.md)
- [C0200 (consider-using-enumerate)](errors/refactoring/C0200.md)
- [C0201 (consider-iterating-dictionary)](errors/refactoring/C0201.md)
- [C1801 (len-as-condition)](errors/refactoring/C1801.md)
- [R1701 (consider-merging-isinstance)](errors/refactoring/R1701.md)
- [R1702 (too-many-nested-blocks)](errors/refactoring/R1702.md)
- [R1703 (simplifiable-if-statement)](errors/refactoring/R1703.md)
- [R1704 (redefined-argument-from-local)](errors/refactoring/R1704.md)
- [R1705 (no-else-return)](errors/refactoring/R1705.md) **[+]**
- [R1706 (consider-using-ternary)](errors/refactoring/R1706.md)
- [R1707 (trailing-comma-tuple)](errors/refactoring/R1707.md)
- [R1708 (stop-iteration-return)](errors/refactoring/R1708.md)
- [R1709 (simplify-boolean-expression)](errors/refactoring/R1709.md)
- [R1710 (inconsistent-return-statements)](errors/refactoring/R1710.md) **[+]**
- [R1711 (useless-return)](errors/refactoring/R1711.md)
- [R1712 (consider-swap-variables)](errors/refactoring/R1712.md)
- [R1713 (consider-using-join)](errors/refactoring/R1713.md)
- [R1714 (consider-using-in)](errors/refactoring/R1714.md)
- [R1715 (consider-using-get)](errors/refactoring/R1715.md)
- [R1716 (chained-comparison)](errors/refactoring/R1716.md)
- [R1717 (consider-using-dict-comprehension)](errors/refactoring/R1717.md)
- [R1718 (consider-using-set-comprehension)](errors/refactoring/R1718.md)
- [R1719 (simplifiable-if-expression)](errors/refactoring/R1719.md)
- [R1720 (no-else-raise)](errors/refactoring/R1720.md)
- [R1721 (unnecessary-comprehension)](errors/refactoring/R1721.md)
- [R1722 (consider-using-sys-exit)](errors/refactoring/R1722.md)
- [R1723 (no-else-break)](errors/refactoring/R1723.md)
- [R1724 (no-else-continue)](errors/refactoring/R1724.md)

### Similarities Checker Messages

- [R0801 (duplicate-code)](errors/similarities/R0801.md)

### Spelling Checker Messages

- [C0401 (wrong-spelling-in-comment)](errors/spelling/C0401.md)
- [C0402 (wrong-spelling-in-docstring)](errors/spelling/C0402.md)
- [C0403 (invalid-characters-in-docstring)](errors/spelling/C0403.md)

### Stdlib Checker Messages

- [E1507 (invalid-envvar-value)](errors/stdlib/E1507.md)
- [W1501 (bad-open-mode)](errors/stdlib/W1501.md)
- [W1502 (boolean-datetime)](errors/stdlib/W1502.md)
- [W1503 (redundant-unittest-assert)](errors/stdlib/W1503.md)
- [W1505 (deprecated-method)](errors/stdlib/W1505.md)
- [W1506 (bad-thread-instantiation)](errors/stdlib/W1506.md)
- [W1507 (shallow-copy-environ)](errors/stdlib/W1507.md)
- [W1508 (invalid-envvar-default)](errors/stdlib/W1508.md)
- [W1509 (subprocess-popen-preexec-fn)](errors/stdlib/W1509.md)
- [W1510 (subprocess-run-check)](errors/stdlib/W1510.md)

### String Checker Messages

- [E1300 (bad-format-character)](errors/string/E1300.md)
- [E1301 (truncated-format-string)](errors/string/E1301.md)
- [E1302 (mixed-format-string)](errors/string/E1302.md)
- [E1303 (format-needs-mapping)](errors/string/E1303.md)
- [E1304 (missing-format-string-key)](errors/string/E1304.md)
- [E1305 (too-many-format-args)](errors/string/E1305.md)
- [E1306 (too-few-format-args)](errors/string/E1306.md)
- [E1307 (bad-string-format-type)](errors/string/E1307.md)
- [E1310 (bad-str-strip-call)](errors/string/E1310.md)
- [W1300 (bad-format-string-key)](errors/string/W1300.md)
- [W1301 (unused-format-string-key)](errors/string/W1301.md)
- [W1302 (bad-format-string)](errors/string/W1302.md)
- [W1303 (missing-format-argument-key)](errors/string/W1303.md)
- [W1304 (unused-format-string-argument)](errors/string/W1304.md)
- [W1305 (format-combined-specification)](errors/string/W1305.md)
- [W1306 (missing-format-attribute)](errors/string/W1306.md)
- [W1307 (invalid-format-index)](errors/string/W1307.md)
- [W1308 (duplicate-string-formatting-argument)](errors/string/W1308.md)
- [W1401 (anomalous-backslash-in-string)](errors/string/W1401.md)
- [W1402 (anomalous-unicode-escape-in-string)](errors/string/W1402.md)
- [W1403 (implicit-str-concat-in-sequence)](errors/string/W1403.md)

### Typecheck Checker Messages

- [E1101 (no-member)](errors/typecheck/E1101.md)
- [E1102 (not-callable)](errors/typecheck/E1102.md)
- [E1111 (assignment-from-no-return)](errors/typecheck/E1111.md)
- [E1120 (no-value-for-parameter)](errors/typecheck/E1120.md)
- [E1121 (too-many-function-args)](errors/typecheck/E1121.md)
- [E1123 (unexpected-keyword-arg)](errors/typecheck/E1123.md)
- [E1124 (redundant-keyword-arg)](errors/typecheck/E1124.md)
- [E1125 (missing-kwoa)](errors/typecheck/E1125.md)
- [E1126 (invalid-sequence-index)](errors/typecheck/E1126.md)
- [E1127 (invalid-slice-index)](errors/typecheck/E1127.md)
- [E1128 (assignment-from-none)](errors/typecheck/E1128.md)
- [E1129 (not-context-manager)](errors/typecheck/E1129.md)
- [E1130 (invalid-unary-operand-type)](errors/typecheck/E1130.md)
- [E1131 (unsupported-binary-operation)](errors/typecheck/E1131.md)
- [E1132 (repeated-keyword)](errors/typecheck/E1132.md)
- [E1133 (not-an-iterable)](errors/typecheck/E1133.md)
- [E1134 (not-a-mapping)](errors/typecheck/E1134.md)
- [E1135 (unsupported-membership-test)](errors/typecheck/E1135.md)
- [E1136 (unsubscriptable-object)](errors/typecheck/E1136.md)
- [E1137 (unsupported-assignment-operation)](errors/typecheck/E1137.md)
- [E1138 (unsupported-delete-operation)](errors/typecheck/E1138.md)
- [E1139 (invalid-metaclass)](errors/typecheck/E1139.md)
- [E1140 (unhashable-dict-key)](errors/typecheck/E1140.md)
- [E1141 (dict-iter-missing-items)](errors/typecheck/E1141.md)
- [I1101 (c-extension-no-member)](errors/typecheck/I1101.md)
- [W1113 (keyword-arg-before-vararg)](errors/typecheck/W1113.md)
- [W1114 (arguments-out-of-order)](errors/typecheck/W1114.md)

### Variables Checker Messages

- [E0601 (used-before-assignment)](errors/variables/E0601.md)
- [E0602 (undefined-variable)](errors/variables/E0602.md)
- [E0603 (undefined-all-variable)](errors/variables/E0603.md)
- [E0604 (invalid-all-object)](errors/variables/E0604.md)
- [E0611 (no-name-in-module)](errors/variables/E0611.md)
- [E0633 (unpacking-non-sequence)](errors/variables/E0633.md)
- [W0601 (global-variable-undefined)](errors/variables/W0601.md)
- [W0602 (global-variable-not-assigned)](errors/variables/W0602.md)
- [W0603 (global-statement)](errors/variables/W0603.md)
- [W0604 (global-at-module-level)](errors/variables/W0604.md)
- [W0611 (unused-import)](errors/variables/W0611.md)
- [W0612 (unused-variable)](errors/variables/W0612.md)
- [W0613 (unused-argument)](errors/variables/W0613.md)
- [W0614 (unused-wildcard-import)](errors/variables/W0614.md)
- [W0621 (redefined-outer-name)](errors/variables/W0621.md)
- [W0622 (redefined-builtin)](errors/variables/W0622.md)
- [W0623 (redefine-in-handler)](errors/variables/W0623.md)
- [W0631 (undefined-loop-variable)](errors/variables/W0631.md)
- [W0632 (unbalanced-tuple-unpacking)](errors/variables/W0632.md)
- [W0640 (cell-var-from-loop)](errors/variables/W0640.md)
- [W0641 (possibly-unused-variable)](errors/variables/W0641.md)
- [W0642 (self-cls-assignment)](errors/variables/W0642.md)
