**Use Case Name: Validate A Science Plan**

**ID:** 4

**Importance Level:** High

--------------------------------------------------------

**Primary Actor:** Science Observer

**Use Case Type:** Detail, Essential

--------------------------------------------------------

**Stakeholders and Interests:**

Science Observer - receives a TESTED science plan and wants to check if all the information is valid.

--------------------------------------------------------

**Brief Description:**

This use case summarizes the activities involved in validating a science plan.

--------------------------------------------------------

**Trigger:** A science plan passed the testing and needs to be validated.

**Type:** External

--------------------------------------------------------

**Relationships:**

**Association:** Science Observer\
**Include:** - \
**Extend:** -\
**Generalization:** -

--------------------------------------------------------

**Normal Flow of Events:**

1. The science observer opens the Gemini Telescope Control System.
2. The science observer browses the TESTED science plans.
3. The science observer receives a list of TESTED science plans.
4. The science observer selects a science plan to validate.
5. The science observer checks the details of the science plan manually.
6. The science observer validates the science plan.

--------------------------------------------------------

**Sub flows:**

5.1. The science observer validates and checks the feasibility and the correctness of the science plan.

--------------------------------------------------------

**Alternate/Exceptional Flow:**

6.a. If the science plan is valid, the science observer validates the science plan.\
6.b. If the science plan is invalid, the science observer rejects the science plan.