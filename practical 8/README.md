AIM

To generate swarm-like particles and bubble masses using Blender’s particle systems with force fields and driver expressions.

PROCEDURE

Swarm

1. Add Plane (ground) + Sphere (emitter).


2. Sphere → Particle System → Emitter, Number=2000, Lifetime=200.


3. Add Turbulence (Strength 5, Size 2) + Wind (Strength 2).


4. Right-click Turbulence Strength → Add Driver → Graph Editor → Add Noise Modifier (Scale 50, Strength 10).


5. Render particles as tiny glowing spheres (Emission shader).



Bubbles

1. Add big Cube (container) + small Sphere inside (emitter).


2. Particle System → Number=500, Lifetime=150.


3. Physics → Brownian=1.0, Drag=0.2.


4. Field Weights → Gravity = -0.3 → bubbles rise.


5. Add Turbulence → Strength 2 → wobble effect.


6. Driver on Particle Scale → Noise Modifier for size variation.


7. Assign transparent material (Transmission=1, IOR=1.333).



RESULT

Swarm: Particles moved chaotically like fireflies/insects.

Bubbles: Particles rose with wobble and varied size like underwater bubbles.
