for i in `seq 1775 2013`
do
    echo "wyniki/n$i"
    echo "($i, " >> "wyniki.txt"
    cat "wyniki/n$i.txt" | egrep 'Zanalizowano ' | sed 's/\./, /g' | sed 's/[^0-9,]//g' >> "wyniki.txt"
    cat "wyniki/n$i.txt" | egrep 'Nie rozpoznano ' | sed 's/\./\),/g' | sed 's/[^0-9\),]//g' >> "wyniki.txt"
done
