# the standard input according to the problem statement.

read -r N
Pi_array=()
for (( i=0; i < $N; i++)); do
    read -r Pi
    Pi_array[i]="$Pi"
done
Pi_array=($(printf '%s\n' "${Pi_array[@]}" | sort -n))

min_diff=9999999
for (( i=1; i < $N; i++)); do
    diff=$((Pi_array[i]-Pi_array[i - 1]))
    abs_diff=${diff#-}
    if ((abs_diff < min_diff)); then
        min_diff=$abs_diff
    fi
done
echo "$min_diff"
