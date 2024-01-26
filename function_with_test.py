def special_list(input_list: list[int]) -> list[int]:
  """
  Processes a list of integers and returns a new list with elements at certain positions removed. 
  Specifically, elements at positions which are multiples of 2 or 3 (considering zero-based indexing) are removed. 
  The function checks for two constraints: the input must be a list of integers, and its length must be a multiple of 10. 
  If these constraints are not met, appropriate errors are raised.

  @params:
  - input_list (list[int]): A list of integers. The length of this list should be a multiple of 10. 

  @return:
  - list[int]: A new list derived from the input list but with elements at positions that are multiples of 2 or 3 removed.

  Raises:
  - ValueError: If 
    - the length of `input_list` is not a multiple of 10 or 
    - any element in `input_list` is not an integer or 
    - `input_list` is None.
    
  Precondition:
  - Position indexing starts from 0 (zero-based indexing).
  
  Example:
  >>> special_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  [1, 5, 7]
  """
  if input_list is None:
      raise ValueError("Input should not be None")

  if len(input_list) % 10 != 0:
      raise ValueError("Length of the input should be a multiple of 10!")

  for item in input_list:
      if not isinstance(item, int):
          raise ValueError("All elements must be integers")

  return [v for i, v in enumerate(input_list) if i % 2 != 0 and i % 3 != 0]








def special_list_test():

  
  # test if it returns ValueError if `input_list` is None.
  try:
      special_list(None)
      assert False, "ValueError expected but not raised"
  except ValueError:
      pass  # Passes if ValueError is raised, which is expected
  except Exception as e:
      assert False, f"Unexpected exception raised: {e}"
  
  # test if it returns valueError if the length of `input_list` is not a multiple of 10
  for i in range(1, 100, 10):
      test_list = list(range(i))
      try:
          special_list(test_list)
          assert False, "ValueError expected but not raised"
      except ValueError:
          pass  # Passes if ValueError is raised, which is expected
      except Exception as e:
          assert False, f"Unexpected exception raised: {e}"

  # test if it returns valueError if any element in `input_list` is not an integer
  try:
      special_list([1, 2, "abcd", 4, 5, 6, 7, 8, 9, 10])  # Length is 10
      assert False, "ValueError expected but not raised"
  except ValueError:
      pass  # Passes if ValueError is raised, which is expected
  except Exception as e:
      assert False, f"Unexpected exception raised: {e}"

  # some base cases
  assert special_list([]) == []
  assert special_list([0,1,2,3,4,5,6,7,8,9]) == [1, 5, 7]
  assert special_list([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == [1,5,7,11,13,17,19]

  # Test for a very large list
  large_list = list(range(100))
  expected_output = [v for i, v in enumerate(large_list) if i % 2 != 0 and i % 3 != 0]
  assert special_list(large_list) == expected_output

special_list_test()
