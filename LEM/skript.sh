#sam jest tu : ftp://ftp.mimuw.edu.pl/pub/users/polszczyzna/SAM-95/

for i in `seq 1775 2013`
do
    echo "tresci/$i"
    cat "tresci/$i.txt" | sed 's/[^a-zA-ZęółśążźćńŻŹĆŃŁŚĄĘÓ]/ /g'  > "tresci/n$i.txt"
    ./sam34 -b tresci/n$i.txt > "wyniki/n$i.txt"
done
    
