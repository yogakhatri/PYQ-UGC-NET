# Question 2

*UGC NET CS · 2011 Dec Paper 3 · Software Process Models · Software Process and Waterfall; OR Two-Phase Locking*

(a) What do you mean by a software process ? What is the diffe rence between a methodology and a process ? What problem will a Software Developme nt house face if it does not follow any systematic process in its software development efforts ? (b) Which are the major phases in the waterfall model of softwa re development ? Which phase consumes the maximum effort ? OR (a) Show that a static two phase locking schedule satisfies t he condition for dynamic two phase locking. Is the converse true ? (b) Propose a multi version protocol base on locking. Prove that the protoc ol is safe. Compare the performance of this protocol with the one based on time stemp ordering. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Both alternatives are explained below**

## Solution

**Alternative A — Software process and waterfall**

A software process is the organized set of activities, roles, work products, controls and feedback used to develop and maintain software. A methodology is a more prescriptive package of practices, modelling techniques, notation and guidance for carrying out that process. In short, the process says what lifecycle work and control points exist; a methodology gives a disciplined way to perform them.

Without a systematic process, requirements are missed, estimates and responsibilities become unstable, designs are inconsistent, changes are uncontrolled, testing begins late, defects recur, documentation disappears and progress cannot be measured. The result is rework, schedule and cost overruns, poor maintainability and dependence on individual developers.

A conventional waterfall proceeds through feasibility/planning, requirements analysis and specification, architectural and detailed design, implementation and unit testing, integration/system testing, deployment, and operation/maintenance. Across the whole product life, maintenance usually consumes the largest effort because correction, adaptation and enhancement continue for years. In a development-only accounting, implementation and testing dominate, so the scope of the estimate should be stated.

**Alternative B — Two-phase locking and multiversion locking**

Static 2PL obtains every required lock before a transaction starts. Dynamic 2PL has a growing phase that acquires locks and a shrinking phase that releases them; after the first release, no new lock may be obtained. Static 2PL is therefore a special case of dynamic 2PL: all acquisitions occur before any release. The converse is false. A dynamic transaction may lock A, later lock B, then release both; it obeys 2PL but did not acquire all locks before starting.

One safe multiversion 2PL design is: retain committed versions; readers select the newest committed version visible to them and do not overwrite it; a writer obtains an exclusive write lock, creates a private new version, and holds its write locks until commit or abort. At commit the versions become visible atomically; abort discards them. Exclusive locks serialize conflicting writers, strict lock holding prevents dirty writes, and readers observe only committed states, so the resulting dependency order is equivalent to a serial commit/lock order. Garbage collection removes versions only when no active reader can need them.

Compared with multiversion timestamp ordering, MV2PL uses locking and may block or deadlock, requiring detection or prevention. It often avoids needless read-write blocking and may abort less when conflicts are temporary. MV timestamp ordering never deadlocks and chooses versions using transaction timestamps, but a write that violates timestamp/read rules must abort even when waiting might have succeeded.

## Key Points

- Process organizes lifecycle work; methodology prescribes practices.
- Static 2PL is a subset of dynamic 2PL.
- Safe MV2PL combines committed snapshots with strict writer locking.

## Common mistakes to avoid

Do not equate a process with a single programming method. Do not omit maintenance when discussing lifetime effort. Static 2PL is stronger than ordinary dynamic 2PL, not equivalent to it. A multiversion protocol is unsafe if readers can see uncommitted versions or if conflicting writers publish without serialization.
