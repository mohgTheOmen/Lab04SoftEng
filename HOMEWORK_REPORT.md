# Lab 4 Homework: AI-Assisted Bug Detection and Repair

## Objective
Create a Bug Fixer skill that uses bug reports from the Bug Finder skill.
Generate regression tests with the Test Writer skill and verify that
the automatically repaired code passes all tests.

## Tools
- Model: Qwen3-4B-Instruct-2507
- Bug Finder skill
- Test Writer skill
- Bug Fixer skill
- pytest

## Results

| Difficulty | Function | Bug | Before Fix | After Fix |
|---|---|---|---|---|
| Easy | calculate_discount | Incorrect percentage calculation | FAIL | PASS |
| Easy | is_valid_age | Incorrect boundary comparison | FAIL | PASS |
| Medium | average_scores | Division by zero on empty input | FAIL | PASS |
| Hard | find_user | SQL injection | FAIL | PASS |
| Hard | safe_read_file | Path traversal | FAIL | PASS |

## Summary
- Functions tested: 5
- Bugs identified: 5
- Tests generated: 5
- Tests failing before repair: 5
- Tests passing after repair: 5
- Final regression test success rate: 100%

## Observations
The initial Test Writer generated some tests that did not expose the
original bugs. Improving its instructions produced effective regression
tests.

The initial Bug Fixer also produced an incomplete path traversal fix
and, during another attempt, invalid Python syntax. Refining the skill
instructions allowed Qwen to generate a solution that passed all five tests.

## Conclusion
The three-skill workflow successfully identified, tested, and repaired
five Python bugs of varying difficulty.

The experiment also demonstrated the importance of validating
AI-generated tests and checking generated source code before applying it.
