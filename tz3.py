def read_file(filename: str):
    nums = []
    with open(filename) as file:
        for num in list(file)[0].split(" "):
            nums.append(int(num))
    return nums


def _min(nums: list):
    min_i = nums[0]
    for i in nums:
        if i < min_i:
            min_i = i
    return min_i


def _max(nums: list):
    max_i = nums[0]
    for i in nums:
        if i > max_i:
            max_i = i
    return max_i


def _sum(nums: list):
    sum_i = 0
    for i in nums:
        sum_i += i
    return sum_i


def _prod(nums: list):
    prod_i = 1
    for i in nums:
        prod_i *= i
    return prod_i


def main():
    data = read_file('data.txt')
    print(f"Минимальное: {_min(data)}")
    print(f"Максимальное: {_max(data)}")
    print(f"Сумма: {_sum(data)}")
    print(f"Произведение: {_prod(data)}")


if __name__ == '__main__':
    main()
