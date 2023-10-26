#!/usr/bin/awk -f

BEGIN { RS = "\n\n"; FS = "\n"; ORS = RS; OFS = FS; STAGE = 1 }

/^$/ { next }
 
STAGE == 1 {
NUM=$2
sub(/=.*/, "", NUM)
A[NUM] = $0
#NUM=$3
#sub(/=.*/, "", NUM)
#A[NUM] = $0
}

STAGE == 2 {
NUM=$2
sub(/=.*/, "", NUM)
if (A[NUM]) {
    split(A[NUM], B)
    print B[1] " => " $1, $2, $3
    delete A[NUM]
}
}

END {
for (NUM in A) {
    if (A[NUM]) print A[NUM]
}
}
