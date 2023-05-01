<?php
    # While
    echo "while: ";
    $i = 0;
    while ($i < 10) {
        echo $i;
        $i++;
    }

    #do...While
    echo "<br>do...while: ";
    $i = 0;
    do { echo $i; 
        $i++;
    } while ($i < 10);

    #for 
    echo "<br>for: ";
    for ($i = 0; $i < 10; $i++){echo $i;}

    #forech
    echo "<br>forech: ";
    $i = [0,1,2,3,4,5,6,7,8,9];
    foreach ($i as $j){
        echo $j;
    }