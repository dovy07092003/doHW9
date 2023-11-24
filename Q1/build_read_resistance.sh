# Name build_read_resistance.sh
#!/bin/bash
echo "Building file for AnalogIn.cpp and read_resistance.cpp"
g++ -Wall AnalogIn.cpp read_resistance.cpp -o read_resistancecpp
echo "Done. The name is read_resistancecpp"
