#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list[list[int]]): The n x n matrix to be rotated.

    Returns:
        None: The matrix is modified in place.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        row.reverse()

@app.route('/rotate-matrix', methods=['POST'])
def rotate_matrix_endpoint():
    """
    Flask endpoint to rotate a 2D matrix.
    
    Request:
        JSON body with a 2D matrix.
    
    Response:
        JSON body with the rotated matrix.
    """
    try:
        data = request.get_json()
        matrix = data.get("matrix")
        
        if not matrix or not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            return jsonify({"error": "Invalid input. Provide a 2D matrix in JSON format."}), 400
        
        rotate_2d_matrix(matrix)
        
        return jsonify({"rotated_matrix": matrix}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
