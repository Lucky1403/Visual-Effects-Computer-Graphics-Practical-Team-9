AIM

To create and visualize foliage (grass/trees), fire with smoke, and smoke-only simulations in Blender using Particle Systems / Geometry Nodes for foliage and Mantaflow (Gas) for fire & smoke.

APPARATUS

Blender 3.6 LTS (recommended) or Blender 4.4.0 (Mantaflow liquid unstable in 4.4)

Plane (ground), cube/sphere (emitters), domain cube

Cycles renderer for realistic volumetrics


PROCEDURE

Foliage

1. Add Plane → Scale large.


2. Create Grass Blade (flat small plane).


3. Ground → Particle System → Hair → Render As Object → Instance GrassBlade.


4. Adjust count, clumping, randomness.



Fire & Smoke

1. Add small cube (emitter) inside large cube (domain).


2. Emitter → Physics → Fluid → Flow → Fire+Smoke, Behavior = Inflow.


3. Domain → Fluid → Domain → Gas. Resolution 32–64.


4. Cache → All → Bake All.


5. Shader: Principled Volume → adjust density, blackbody intensity.



Smoke Only

Same as above, but Flow Type = Smoke.

Add Turbulence force field → Strength 2–6.


RESULT

Foliage, fire, and smoke were successfully simulated.
