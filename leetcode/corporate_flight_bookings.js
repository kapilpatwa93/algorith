// 1109. Corporate Flight Bookings
//

/**
 * @param {number[][]} bookings
 * @param {number} n
 * @return {number[]}
 */
var corpFlightBookings = function(bookings, n) {
    const flight = Array(n).fill(0)
    for (let i = 0; i < bookings.length; i++) {
        for (let j = bookings[i][0]-1; j < bookings[i][1] ; j++) {
            flight[j] = flight[j] + bookings[i][2]
        }
    }
    return flight;
};
function main() {
    const bookings = [[1,2,10],[2,3,20],[2,5,25]];
    const n = 5     
    corpFlightBookings(bookings,n)
}
main()
