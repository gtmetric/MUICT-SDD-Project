**Use Case Name: Create a Science Plan**

**ID:** 2

**Importance Level:** High

--------------------------------------------------------

**Primary Actor:** Astronomer

**Use Case Type:** Detail, Essential

--------------------------------------------------------

**Stakeholders and Interests:**

Astronomer - wants to create a science plan to collect astronomical data.

--------------------------------------------------------

**Brief Description:**

This use case describes how an astronomer creates a science plan.

--------------------------------------------------------

**Trigger:** The astronomer would like to create a science plan to collect astronomical data.

**Type:** External

--------------------------------------------------------

**Relationships:**

**Association:** Astronomer\
**Include:** -\
**Extend:** -\
**Generalization:** -

--------------------------------------------------------

**Normal Flow of Events:**

1. The astronomer opens the Gemini Telescope Control System.
2. The astronomer navigates to the Create Science Plan page.
3. The astronomer enters the creator's name.
4. The astronomer enters the submitter's name.
5. The astronomer enters the funding.
6. The astronomer enters the objectives of the science plan.
7. The astronomer browses the star systems.
8. The astronomer receives a list of star systems.
9. The astronomer selects a star system.
10. The astronomer sets the schedule (date and time).
11. The astronomer selects the telescope location.
12. The astronomer enters the image processing requirements.
13. The astronomer creates the science plan.

--------------------------------------------------------

**Sub flows:**

10.1. The astronomer enters the start date and time.\
10.2. The astronomer enters the end date and time.\
12.1. The astronomer selects a preferred file type.\
12.2. The astronmer selects a file quality.\
12.3. The astronmer selects a prefered color type.\
12.4. The astronomer determines the image processing properties including contrast, brightness, saturation, exposure, highlights, shadows, whites, blacks, luminance, and hue.

--------------------------------------------------------

**Alternate/Exceptional Flow:**

10.a. If the end date has come before the start date, the astronomer must enter a new schedule.\
12.a. If the B&W mode is selected, the astronomer can adjust all the image processing properties except brightness, saturation, luminance and hue.\
12.b. If the Color mode is selected, the astronomer can adjust all the image processing properties except highlights, shadows, whites, and blacks.