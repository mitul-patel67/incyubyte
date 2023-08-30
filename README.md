# incyubyte Assesment
#Mitul Patel

TEST CASE
Test Case 1: Basic Movement

Starting Position: (0, 0, 0)
Initial Direction: N

Commands: ["f", "r", "u", "b", "l"]

Expected Final Position: (0, 1, -1)
Expected Final Direction: N

**************************************
Test Case 2: Complex Movement

Starting Position: (10, 10, 0)
Initial Direction: N

Commands: ["f", "r", "f", "r", "f", "l", "f", "l", "b", "b"]

Expected Final Position: (10, 10, 0)
Expected Final Direction: W

**************************************
Test Case 3: Up and Down

Starting Position: (0, 0, 0)
Initial Direction: N

Commands: ["u", "f", "d", "f"]

Expected Final Position: (0, 1, 0)
Expected Final Direction: N

**************************************
Test Case 4: Back and Forth

Starting Position: (-2, 4, 1)
Initial Direction: W

Commands: ["b", "f", "b", "f"]

Expected Final Position: (-2, 4, 1)
Expected Final Direction: W
**************************************
Test Case 5: Turning and Moving

Starting Position: (5, -3, 2)
Initial Direction: E

Commands: ["l", "f", "u", "r", "b"]

Expected Final Position: (5, -2, 3)
Expected Final Direction: S
