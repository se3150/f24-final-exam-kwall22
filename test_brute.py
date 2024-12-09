import pytest
from brute import Brute
from unittest.mock import Mock
import hashlib, random, string, time

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")
    
    @pytest.fixture
    def hardest_cracker():
        #as hard as it gets alphabet = string.ascii_letters + string.digits
        return Brute(string.ascii_letters + string.digits)
    
    def describe_bruteOnce():
        def it_returns_true_on_successful_attempt_with_simple(cracker):
            c = cracker.bruteOnce("TDD")
            assert c == True
        def it_returns_true_on_successful_attempt_with_hard(hardest_cracker):
            c = hardest_cracker.bruteOnce(string.ascii_letters + string.digits)
            assert c == True        
        def it_returns_false_on_bad_attempt_with_simple(cracker, hardest_cracker):
            c = cracker.bruteOnce("laksdfh")
            assert c == False
        def it_returns_false_on_bad_attempt_with_hard(hardest_cracker):
            c = hardest_cracker.bruteOnce("kahsdkf")
            assert c == False

    def describe_bruteMany():
        def it_doesnt_allow_negative_limit(cracker):
            c = cracker.bruteMany(limit=-2)
            assert c == -1

        def it_returns_positive_float_on_success(cracker):
            seconds = cracker.bruteMany()
            assert isinstance(seconds, float)
            assert seconds > 0
        
        def it_returns_negative_one_on_fail(hardest_cracker):
            fail = hardest_cracker.bruteMany()
            assert isinstance(fail, int)
            assert fail == -1
        #have to mock the hash which is in bruteOnce
        #have to mock random guess 
        #all of them run limit times in brute many 
        def it_uses_hash_in_bruteOnce_for_each_loop(mocker, cracker):
            #have to mock brute once to use hash from brute many, fail it so it runs the loop limit amount of times
            mock_fail_brute_once = mocker.patch.object(cracker, 'bruteOnce', return_value=False)
            cracker.bruteMany(limit=3)
            assert mock_fail_brute_once.call_count == 3
        
        def it_uses_random_guess_inside_brute_once_for_each_loop(mocker, cracker):
            mock_fail_brute_once = mocker.patch.object(cracker, 'bruteOnce', return_value=False)
            mock_random_guess = mocker.patch.object(cracker, 'randomGuess', return_value="mock_guess")
            cracker.bruteMany(limit=3)
            assert mock_random_guess.call_count == 3
            assert mock_fail_brute_once.call_args_list == [mocker.call("mock_guess") for _ in range(3)]
        

            


