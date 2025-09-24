AIM

To simulate water, smoke, and sparks using Mantaflow liquid, Mantaflow gas, and Blender’s particle systems.

PROCEDURE

Water

1. Add Plane (ground), small Sphere (inflow), and big Cube (domain).


2. Domain → Fluid → Domain → Type = Liquid, Resolution 32.


3. Sphere → Flow → Liquid → Inflow.


4. Plane → Effector → Collision.


5. Cache → Bake All.


6. Enable Mesh → Shading → Transmission = 1, IOR = 1.333.



Smoke

1. Domain → Gas.


2. Emitter → Flow → Smoke (Inflow).


3. Domain Gas Settings → Buoyancy 1, Vorticity 2.


4. Add Turbulence → Strength 5.


5. Bake All.



Sparks

1. Add Sphere (emitter) above Plane.


2. Particles → New → Number = 2000, Start=1, End=2, Lifetime=20.


3. Plane → Collision.


4. Create small glowing icosphere (emission shader).


5. Particle Render As → Object → instance the glowing sphere.


6. Add Motion Blur.



RESULT

Realistic water, smoke, and spark simulations were created with Mantaflow and particle systems.

