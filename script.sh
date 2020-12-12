x=$(csvcut -c 1 Nodes.csv)
y=$(echo $x | tr '\n' ' ')
y="${y:14}"
z="${y// /|}"
z="${z::-1}"
csvgrep -c 1 -r $z -i Nodes_Complete.csv > stateNodes.csv

