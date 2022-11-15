vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals * sin(time * 3)/10, 1.0)).xyz;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * sin(time * 3)/10, 1.0);

}
'''

fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));

    fragColor = texture(tex, UVs) * intensity;
}
'''

toon_shader = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight -pos));
    if(intensity < 0.25){
        intensity = 0.4;
    }
    else if(intensity < 0.5){
        intensity = 0.6;
    }
    else if(intensity < 0.75) {
        intensity = 0.8;
    }
    else if(intensity <= 1){
        intensity = 1.5;
    }
    fragColor = texture(tex, UVs) * intensity;
}
'''
electry_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight -pos));

    vec4 textr = texture(tex, UVs);

    fragColor = textr + vec4(0,1,0,0) * intensity;

}
'''

multicolor_shader=  """
#version 450

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight -pos));
    float r =  3.14 * 12;
    float g = 3.14 * 8;
    float b = 1.0;

    fragColor = vec4(r, g, b, 1.0) * intensity;
}
"""