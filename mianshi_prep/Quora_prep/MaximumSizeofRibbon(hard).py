# binary search?
# each item // the number, sum should be bigger than k
# if sum > k, size can be bigger, if sum < k, size should be smaller
# smallest is 0, biggest is max

def solution(A,k):
    smallest = 1
    biggest = max(A)

    def part(size):
        return sum([item//size for item in A])

    while smallest<=biggest:
        mid = (smallest+biggest)//2
        if part(mid) == k:
            return mid;
        if part(mid) > k:
            smallest = mid+1
        else:
            biggest = mid-1

    return 0

if __name__ == "__main__":
    A = [1,2,3,4,9]
    k = 5
    print (solution(A,k))
