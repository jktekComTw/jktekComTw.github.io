// Get WebGL context
var canvas = document.getElementById('webgl-canvas');
var gl = canvas.getContext('webgl');

if (!gl) {
    console.error('WebGL not supported in this browser.');
    return;
}

// Vertex shader program
var vsSource = `
    attribute vec4 aVertexPosition;
    uniform mat4 uModelViewMatrix;
    uniform mat4 uProjectionMatrix;
    void main() {
        gl_Position = uProjectionMatrix * uModelViewMatrix * aVertexPosition;
    }
`;

// Fragment shader program
var fsSource = `
    void main() {
        gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0); // white color
    }
`;

// Initialize shaders...
// Initialize buffers...
// Define the cube's geometry...

var rotation = 0.0;

function render() {
    rotation += 0.01; // Change this value to adjust rotation speed

    // Clear the canvas
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

    // Set up the rotation matrix
    var modelViewMatrix = mat4.create();
    mat4.rotate(modelViewMatrix, modelViewMatrix, rotation, [1, 1, 1]); // Rotate around x, y, and z axis

    // Set the shader uniforms
    gl.uniformMatrix4fv(programInfo.uniformLocations.modelViewMatrix, false, modelViewMatrix);

    // Draw the cube...
    
    requestAnimationFrame(render);
    
}

render();
