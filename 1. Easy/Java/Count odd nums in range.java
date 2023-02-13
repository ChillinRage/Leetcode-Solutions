public int countOdds(int low, int high) {
    //if both low and high are odd,
    //then count = (high - low)/2 + 1
        
    //if only one of them is odd,
    //then count = (high - low)/2 + 1
        
    //if both are even,
    //then count = (high - low)/2
    
    int count = (high - low) / 2;

    if ( !( is_even(low) && is_even(high) ) ) {
            count++;
    }

    return count;
}

    
static boolean is_even(int num) {
    return (num % 2 == 0);
}