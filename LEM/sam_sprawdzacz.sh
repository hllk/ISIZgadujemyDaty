for i in `seq 1 1042`
do
    echo "dev/$i.txt"
    cat "dev/$i.txt" | egrep '^[0-9]{4}' > wynikitmp.txt
    cat "dev/$i.txt" | egrep '[a-z]' | sed 's/[^a-zA-ZęółśążźćńŻŹĆŃŁŚĄĘÓ]/ /g' > tmp.txt
    ./sam34 -b tmp.txt >> wynikitmp.txt
    cat wynikitmp.txt | egrep 'Zanalizowano |rozpoznano |1[7-9][0-9]{2}|20[01][0-9]' | sed 's/[^0-9,]//g' | python sam_sprawdzacz.py >> wynikiOstateczne.txt
done

    
