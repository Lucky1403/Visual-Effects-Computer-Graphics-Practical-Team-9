import pybullet as p
import pybullet_data
import numpy as np

# Step 2: Initialize
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
plane_id = p.loadURDF("plane.urdf")
p.setPhysicsEngineParameter(fixedTimeStep=1.0 / 240.0)

# Step 3: Create Rigid Debris
box_half_extents = [0.1, 0.1, 0.1]
box_visual_shape = p.createVisualShape(p.GEOM_BOX, halfExtents=box_half_extents)
box_collision_shape = p.createCollisionShape(p.GEOM_BOX, halfExtents=box_half_extents)
for i in range(50):
    pos_x = np.random.uniform(-1, 1)
    pos_y = np.random.uniform(-1, 1)
    pos_z = np.random.uniform(2, 5)
    p.createMultiBody(
        baseMass=1,
        baseCollisionShapeIndex=box_collision_shape,
        baseVisualShapeIndex=box_visual_shape,
        basePosition=[pos_x, pos_y, pos_z]
    )

# Step 4: Create Semi-Rigid Debris (a chain)
num_links = 10
link_half_extents = [0.05, 0.1, 0.05]
link_mass = 0.1
link_visual_shape = p.createVisualShape(p.GEOM_BOX, halfExtents=link_half_extents)
link_collision_shape = p.createCollisionShape(p.GEOM_BOX, halfExtents=link_half_extents)
prev_link_id = p.createMultiBody(
    baseMass=0,
    baseCollisionShapeIndex=link_collision_shape,
    baseVisualShapeIndex=link_visual_shape,
    basePosition=[0, 0, 5]
)
for i in range(1, num_links):
    link_id = p.createMultiBody(
        baseMass=link_mass,
        baseCollisionShapeIndex=link_collision_shape,
        baseVisualShapeIndex=link_visual_shape,
        basePosition=[0, i * -0.2, 5]
    )
    p.createConstraint(
        parentBodyUniqueId=prev_link_id,
        parentLinkIndex=-1,
        childBodyUniqueId=link_id,
        childLinkIndex=-1,
        jointType=p.JOINT_POINT2POINT,
        jointAxis=[0, 1, 0],
        parentFramePosition=[0, -0.1, 0],
        childFramePosition=[0, 0.1, 0]
    )
    prev_link_id = link_id

# Step 5: Run
for i in range(10000):
    p.stepSimulation()
    # You can also use p.sleep() for a fixed frame rate, e.g., p.sleep(1./240.)
    
p.disconnect()