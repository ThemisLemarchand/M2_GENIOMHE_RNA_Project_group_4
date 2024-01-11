#rm output.csv
for f in $(ls data/angles/TestSet); 
    do 
        cp data/angles/TestSet/${f} temp
       # cat temp
        sed -i '1d' temp        
        cut -d "," -f 8,20 temp >> output_test.csv;
done;