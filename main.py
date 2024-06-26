def rpn(x):
  stack = [0] * len(x)
  pointer = -1 
  
  def nextSymbol(expr, start):
      while start < len(expr) and expr[start] == ' ':
          start += 1
      if start >= len(expr):
          return '', start
      if expr[start] in '+-*/':
          return expr[start], start + 1
      end = start
      while end < len(expr) and expr[end] not in ' +-*/':
          end += 1
      return expr[start:end], end

  index = 0
  while index < len(expression):
      symbol, index = nextSymbol(expression, index)
      if symbol in {'+', '-', '*', '/'}:
          b = stack[pointer]
          pointer -= 1
          a = stack[pointer]
          if symbol == '+':
              stack[pointer] = a + b
          elif symbol == '-':
              stack[pointer] = a - b
          elif symbol == '*':
              stack[pointer] = a * b
          elif symbol == '/':
              stack[pointer] = a / b
      elif symbol:
          pointer += 1
          stack[pointer] = float(symbol)
  return stack[pointer]

expression = input("type in rpn in form 'a b -' : ")
result = rpn(expression)
print(result)

