def check(cases, fun):
    passed = 0
    for a, b in cases:
        if fun(a) != b:
            print("Failed: Input '" + str(a) + "' did not return '" + str(b) + "'")
        else:
            print("Passed: Correctly returned '" + str(b) + "' for input '" + str(a) + "'!")
            passed += 1
    print("Passed " + str(passed) + " tests out of " + str(len(cases)) + " tests!")

def check2(cases, fun):
    passed = 0
    for a, b in cases:
        if fun(a[0], a[1]) != b:
            print("Failed: Input '" + str(a[0]) + "' and '" + str(a[1]) + "' did not return '" + str(b) + "'")
        else:
            print("Passed: Correctly returned '" + str(b) + "' for input '" + str(a[0]) + "' and '" + str(a[1]) + "'!")
            passed += 1
    print("Passed " + str(passed) + " tests out of " + str(len(cases)) + " tests!")

def reverse_test(fun):
    cases = [
    ['hello', 'olleh'], ['Howdy', 'ydwoH'],
    ['Greetings from Earth', 'htraE morf sgniteerG']]
    check(cases, fun)

def factorialize_test(fun):
    cases = [
    [5, 120], [10, 3628800], [20, 2432902008176640000], [0, 1]]
    check(cases, fun)

def palindrome_test(fun):
    cases = [
    ['eye', True], ['_eye', True], ['race car', True], ['not a palindrome', False], ['A man, a plan, a canal. Panama', True], ['never odd or even', True], ['nope', False], ['almostomla', False], ['My age is 0, 0 si ega ym.', True], ['1 eye for of 1 eye.', False], ['0_0 (: /-\ :) 0-0', True], ['five|\_/|four', False]]
    check(cases, fun)

def findLongestWord_test(fun):
    cases = [
    ['The quick brown fox jumped over the lazy dog', 6], ['May the force be with you', 5], ['Google do a barrel roll', 6], ['What is the average airspeed velocity of an unladen swallow', 8], ['What if we try a super-long word such as otorhinolaryngology', 19]]
    check(cases, fun)

def titleCase_test(fun):
    cases = [
    ["I'm a little tea pot", "I'm A Little Tea Pot"], ['sHoRt AnD sToUt', 'Short And Stout'], ['HERE IS MY HANDLE HERE IS MY SPOUT', 'Here Is My Handle Here Is My Spout']]
    check(cases, fun)

def largestOfFour_test(fun):
    cases = [
    [[[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]], [27,5,39,1001]], [[[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]],[9, 35, 97, 1000000]]
    ]
    check(cases, fun)

def confirmEnding_test(fun):
    cases = [
    [['Bastian', 'n'], True], [['Connor', 'n'], False], [['Walking on water and developing software from a specification are easy if both are frozen', 'specification'], False], [['He has to give me a new name', 'name'], True], [['Open sesame', 'same'], True], [['Open sesame', 'pen'], False], [['If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing', 'mountain'], False]
    ]
    check2(cases, fun)

def repeatString_test(fun):
    cases = [
    [['*', 3], '***'], [['abc', 3], 'abcabcabc'], [['abc', 4], 'abcabcabcabc'], [['abc', 1], 'abc'], [['*', 8], '********'], [['abc', -2], '']]
    check2(cases, fun)

def truncateString_test(fun):
    cases = [
    [['A-tisket a-tasket A green and yellow basket', 11], 'A-tisket...'], [['Peter Piper picked a peck of pickled peppers', 14], 'Peter Piper...'], [['A-tisket a-tasket A green and yellow basket', len('A-tisket a-tasket A green and yellow basket')], 'A-tisket a-tasket A green and yellow basket'], [['A-tisket a-tasket A green and yellow basket', len('A-tisket a-tasket A green and yellow basket') + 2], 'A-tisket a-tasket A green and yellow basket'], [['A-', 1], 'A...'], [['Absolutely Longer', 2], 'Ab...']]
    check2(cases, fun)

def chunkList_test(fun):
    cases = [
    [[["a", "b", "c", "d"], 2], [["a", "b"], ["c", "d"]]], [[[0, 1, 2, 3, 4, 5], 3], [[0, 1, 2], [3, 4, 5]]], [[[0, 1, 2, 3, 4, 5], 2], [[0, 1], [2, 3], [4, 5]]], [[[0, 1, 2, 3, 4, 5], 4], [[0, 1, 2, 3], [4, 5]]], [[[0, 1, 2, 3, 4, 5, 6], 3], [[0, 1, 2], [3, 4, 5], [6]]], [[[0, 1, 2, 3, 4, 5, 6, 7, 8], 4], [[0, 1, 2, 3], [4, 5, 6, 7], [8]]], [[[0, 1, 2, 3, 4, 5, 6, 7, 8], 2], [[0, 1], [2, 3], [4, 5], [6, 7], [8]]]
    ]
    check2(cases, fun)

def slasher_test(fun):
    cases = [
    [[[1, 2, 3], 2], [3]], [[[1, 2, 3], 0], [1, 2, 3]], [[[1, 2, 3], 9], []], [[[1, 2, 3], 4], []], [[["burgers", "fries", "shake"], 1], ["fries", "shake"]], [[[1, 2, "chicken", 3, "potatoes", "cheese", 4], 5], ["cheese", 4]]]
    check2(cases, fun)

def mutation_test(fun):
    cases = [
    [["hello", "hey"], False], [["hello", "Hello"], True], [["zyxwvutsrqponmlkjihgfedcba", "qrstu"], True], [["Mary", "Army"], True], [["Mary", "Aarmy"], True], [["Alien", "line"], True], [["floor", "for"], True], [["hello", "neo"], False], [["voodoo", "no"], False]
    ]
    check(cases, fun)

def bouncer_test(fun):
    cases = [
    [[7, "ate", "", False, 9], [7, "ate", 9]], [["a", "b", "c"], ["a", "b", "c"]], [[False, None, 0, [], ""], []], [[1, None, False, 2, {}], [1,2]]]
    check(cases, fun)

def destroyer_test(fun):
    cases = [
    [[[1, 2, 3, 1, 2, 3], [2,3]], [1, 1]], [[[1, 2, 3, 5, 1, 2, 3], [2,3]], [1, 5, 1]], [[[3, 5, 1, 2, 2], [2, 3, 5]], [1]], [[[2, 3, 2, 3], [2, 3]], []], [[["tree", "hamburger", 53], ["tree", 53]], ["hamburger"]]]
    check2(cases, fun)

def getIndex_test(fun):
    cases = [
    [[[10, 20, 30, 40, 50], 35], 3], [[[10, 20, 30, 40, 50], 30], 2], [[[40, 60], 50], 1], [[[3, 10, 5], 3], 0], [[[5, 3, 20, 3], 5], 2], [[[2, 20, 10], 19], 2], [[[2, 5, 10], 15], 3]]
    check2(cases, fun)

def rot13_test(fun):
    cases = [
    ["GURQRIZNFGREF", "THEDEVMASTERS"], ["QNGN FPVRAPR!", "DATA SCIENCE!"], ["SERR CVMMN!", "FREE PIZZA!"], ["GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.", "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX."]]
    check(cases, fun)
