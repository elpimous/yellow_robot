# yellow_robot
------------------

          servos initialization config :


    // ROBOT POSE AT STARTUP  !!!
    // **************************
    double shoulder_liedown = 0.0;
    FL_Shoulder.Initialize(2, 90 + shoulder_liedown, 90, 0.0, FL, Shoulder, 1340, 1840, 60, 120);  // 0 | 135 mid - 0 out - 180 in
    FR_Shoulder.Initialize(5, 90 - shoulder_liedown, 90, 0.0, FR, Shoulder, 1300, 1800, 60, 120); // 1 | 135 mid - 180 out - 0 in
    BL_Shoulder.Initialize(8, 90 + shoulder_liedown, 90, 0.0, BL, Shoulder, 1200, 1700, 60, 120);  // 2 | 135 mid - 0 out - 180 in
    BR_Shoulder.Initialize(11, 90 - shoulder_liedown, 90, 0.0, BR, Shoulder, 1300, 1800, 60, 120);  // 3 | 135 mid - 180 out - 0 in
    
    //Elbows
    double elbow_liedown = 25.0;
    FL_Elbow.Initialize(3, elbow_liedown, 0, 0.0, FL, Elbow, 500, 2460, 180.0, 0.0);  // 4 | 135  mid - 0 in front - 180 behind
    FR_Elbow.Initialize(6, elbow_liedown, 0, 0.0, FR, Elbow, 580, 2500, 0.0, 180.0); // 5 | 135  mid - 0 in behind - 180 in front
    BL_Elbow.Initialize(9, elbow_liedown, 0, 0.0, BL, Elbow, 520, 2440, 180.0, 0.0);  // 6 | 135  mid - 0 in front - 180 behind
    BR_Elbow.Initialize(12, elbow_liedown, 0, 0.0, BR, Elbow, 580, 2500, 0.0, 180.0); // 7 | 135  mid - 0 in behind - 180 in front

    //Wrists
    double wrist_liedown = -130;
    FL_Wrist.Initialize(4, wrist_liedown, 0, 0.0, FL, Wrist, 600, 2240, 0.0, -130);  // 8 | 0 straight - 140 bent in
    FR_Wrist.Initialize(7, wrist_liedown, 0, 0.0, FR, Wrist, 2340, 760, 0.0, -130); // 9 | 140 straight - 0 bent in
    BL_Wrist.Initialize(10, wrist_liedown, 0, 0.0, BL, Wrist, 500, 2160, 0.0, -130); // 10 | 0 straight - 140 bent in
    BR_Wrist.Initialize(13, wrist_liedown, 0, 0.0, BR, Wrist, 2500, 810, 0.0, -130); // 11 | 140 straight - 0 bent in


