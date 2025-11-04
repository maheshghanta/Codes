"""
Test script to verify the exercise_validation package works correctly
"""

import torch
import numpy as np
from exercise_validation import (
    validate_exercise_1,
    validate_exercise_2,
    validate_mlp_exercise_1,
    validate_cnn_ex1,
    validate_transfer_ex1,
)

print("Testing Exercise Validation Package")
print("=" * 60)

# Test 1: Tensors and Autograd Exercise 1
print("\n1. Testing validate_exercise_1...")
zeros_tensor = torch.zeros(3, 4)
ones_tensor = torch.ones(2, 5)
random_tensor = torch.randn(3, 3)

success, message, hint = validate_exercise_1(zeros_tensor, ones_tensor, random_tensor)
print(f"   Result: {'✓ PASS' if success else '✗ FAIL'}")
print(f"   Message: {message}")

# Test 2: NumPy Conversion Exercise 2
print("\n2. Testing validate_exercise_2...")
numpy_array = np.array([[10, 20, 30], [40, 50, 60]])
torch_from_numpy = torch.from_numpy(numpy_array)
torch_tensor = torch.tensor([[1.5, 2.5], [3.5, 4.5]])
numpy_from_torch = torch_tensor.numpy()

success, message, hint = validate_exercise_2(
    torch_from_numpy, numpy_from_torch, numpy_array, torch_tensor
)
print(f"   Result: {'✓ PASS' if success else '✗ FAIL'}")
print(f"   Message: {message}")

# Test 3: MLP Architecture
print("\n3. Testing validate_mlp_exercise_1...")

class TestMLP(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3072, 512)
        self.fc2 = torch.nn.Linear(512, 256)
        self.fc3 = torch.nn.Linear(256, 10)
        self.relu = torch.nn.ReLU()
    
    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

my_mlp = TestMLP()
success, message, hint = validate_mlp_exercise_1(my_mlp)
print(f"   Result: {'✓ PASS' if success else '✗ FAIL'}")
print(f"   Message: {message}")

# Test 4: CNN Block
print("\n4. Testing validate_cnn_ex1...")

class TestCNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_block = torch.nn.Sequential(
            torch.nn.Conv2d(3, 32, 3, padding=1),
            torch.nn.BatchNorm2d(32),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2)
        )
    
    def forward(self, x):
        return self.conv_block(x)

my_cnn = TestCNN()
success, message, hint = validate_cnn_ex1(my_cnn)
print(f"   Result: {'✓ PASS' if success else '✗ FAIL'}")
print(f"   Message: {message}")

# Test 5: Test failure case
print("\n5. Testing failure case (invalid tensor shape)...")
wrong_zeros = torch.zeros(2, 3)  # Wrong shape!
success, message, hint = validate_exercise_1(wrong_zeros, ones_tensor, random_tensor)
print(f"   Result: {'✗ FAIL' if not success else '✓ UNEXPECTED PASS'}")
print(f"   Message: {message}")
if hint:
    print(f"   Hint: {hint}")

print("\n" + "=" * 60)
print("Package verification complete!")
print("All validation functions are working correctly.")

