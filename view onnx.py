import os
import onnx

model_path = r"D:\yolov7-python\yolov7-tiny.onnx"
model = onnx.load(model_path)

# Check the model structure
print(onnx.helper.printable_graph(model.graph))

# Get inputs and outputs
for input_tensor in model.graph.input:
    print(f"Input: {input_tensor.name}, Shape: {input_tensor.type.tensor_type.shape}")

for output_tensor in model.graph.output:
    print(f"Output: {output_tensor.name}, Shape: {output_tensor.type.tensor_type.shape}")