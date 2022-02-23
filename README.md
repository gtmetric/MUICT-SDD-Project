# GROUP: Gemini-8

## TEAM MEMBERS:
1. Vidchayada Chaisangkha
2. Varisara Janmatakulwat 
3. Rungsimun Manasboonpermpool
4. Wipada Kaewthong
5. Soksedtha Ly

# ITCS431 Software Design and Development (2020)

## Requirement Analysis of the Gemini System

### Functional requirements

1. To maximize the use of the telescope, the system must invoke operations to run in parallel whenever and wherever possible.

2. When errors occur in requests for service to the OCS, the system should be able to retry sending the requests, and the system should give error or warning messages to the users when the requests for service fail a number of times.

3. There should be a login page for all users to identify their identity before having access to the system. This will allow the system to determine the privileges that the users have when using the system.

4. The system should have the capability to identify safety issues caused by the physical machines and notify the users of the condition of the issues. For example, there should be a warning message when the temperature of some physical units has reached the safety limit.

5. The system must notify the user through the interface when faults in any subsystem are detected. This will allow technical staff to handle the issues before it becomes too serious and difficult to solve.

6. The system must provide operations staff the privileges to access all commands and maintenance procedures in case problems happen. (This also includes direct control of physical units.)

7. The system must allow remote users to submit commands to the Gemini 8m Telescopes scheduler at the Gemini 8m Telescopes site via the Remote User Interface.

8. The system must allow astronomers and science observers to have access to data in the system for data acquisition and data quality assessment. 

9. The system must not allow observing astronomers to send control commands directly to the telescope, but the astronomers must be able to enquire about the status of the telescope or any subsystem at any time.

10. The system must allow Multi-point Monitoring, which means the monitors (people who monitor) can see a duplicate screen of the observers, but the monitors must not be allowed to interfere with the environment of the observers.

11. The system must allow Remote Monitoring, which is the same as multipoint monitoring except that the remote users can pick the information to be displayed.

12. As part of Service Observing, the system must provide a visually-oriented programming environment for observing programs to be developed by astronomers and accessed by general users.

13. The system should also allow remote observers to have a real-time video and voice link with the operators in the control rooms.

14. The system must be secured and able to prevent any intrusion into the system by unauthorized users.

15. The system must have a scheduler to handle the observing commands submitted via the user interface to queue for later execution.

16. The system modules should have predefined self-test specifications to check the normal operation of each release of the system itself.

17. The system must constantly or frequently monitor the active subsystems to ensure that they are operating correctly before sending commands to the subsystems.

18. The system must provide three operational levels to restrict users' access to the system in a controllable manner. The operational levels include Observing level, Maintenance level, and Test level.

19. The system must offer status information both automatically and on request at any required level to the astronomers.

20. Although the system must not allow astronomers to have direct control of the telescope via control commands, the system must allow astronomers to develop programs that have the ability to control the telescope.

21. Instead of the traditional interactive operation, the system must allow the operation to be automated by a sequencer.

22. However, the system should provide some interactions, allowing users to interact with the scheduler instead of the control programs directly.

23. The system should allow operations staff to enable direct interactive operation when needed because it is necessary to include interactive capabilities for some functions although it is preferred to be automated.

24. The system should provide a visual-oriented programming environment for the astronomers to develop the observing programs and for the observers to review and adjust the programs.

25. The system must allow the operations staff to update operations tables and allow the astronomers only to read the tables.

26. The system must support the observing modes provided by the OCS. The observing modes consist of Interactive Observing, Queue-based, Remote Operations, and Service.

27. To support Interactive Observing, the system must provide a visual user interface to the OCS to allow for changes to the viewing program.

28. To support Queue-based Observing, the system must handle the observing programs automatically with little human interaction to maximize the efficiency of the use of the telescope.

29. As part of the Queue-base Observing, the system must provide a full telescope simulator for astronomers to test observing programs before being put into queue for execution. All control software must be provided for the simulation in the virtual telescope as well.

30. The system must allow the observing programs to select observing objects to focus on so that the observing efficiency will be optimized.

31. For Remote Operations, the system must be able to restrict specific operations to specific remote users.

### Non-functional requirements

1. The look and feel of the interface should be homogeneous.

2. The user interface should be easy to use in a safe and simple way.

3. For astronomers, the system should provide an interface simple to learn and secure to use to allow the astronomers to achieve efficient work with data.

4. There should be no conceptual difference between working on-site and remotely.

5. The system should provide the user interface with a night mode to support night staff.

6. The user interface of the system for the science observer should have a quick response, ease of controls, and should be easy to use.

7. Similar functionalities in the system should be presented to the users using similar user interfaces.

8. The system must be able to perform with other package modules from other systems including the online database and the OCS.

9. Since the Access Modes of the OCS are divided into different modes providing different functionalities, the user interface of the new system must be designed separately for each mode. The access modes include Observing, Monitoring, Operation, Planning, Testing, and Administrative modes.

10. The system needs near-line processing and off-line processing for data and images.

11. The security of remote operations must be carefully considered and tested.

***Note:** The non-functional requirements below may not be necessary for this project.*

12. Some form of an online image (or pixel) quick-look analysis is required to make efficient use of the telescope so that it can support different observing modes and versatility requirements.

13. The system must allow a full readout of the detector to be done in about 2 or 3 minutes.

14. The system must support concurrent data access and display transferred on LAN to reach a transfer rate of 20-40 Mbits/second.

15. The system must allow fast transmission of rough images every 0.5 seconds.

16. The system must allow all commands to be accepted or rejected within 2 seconds and before the corresponding action occurs.

17. Status display update must be within 4 seconds at the local stations.

18. Requests of subsystems for status information must be answered within 5 seconds and be possible in maintenance level operation.

19. The communication interface between the IOCs and Unix workstations must be based on Internet Messaging Program (IMP).

20. The user interface should quickly respond to meet the response time requirements of the entire system.

21. The system must allow the maximum acceptance detector readout time, about 0.1 seconds, to be achieved.
