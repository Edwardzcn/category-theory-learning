Require Import List.
Require Import Compose.
Require Import Nat.
Module Monoid.
  Check Compose.comp.
  (* Here dot means mappend in ctfp, one means mappend in ctfp *)
  Class Monoid {A:Type} (dot: A->A->A) (one: A)   := {
    (* dot satisfy assoc *)
    dot_assoc:
      forall x y z:A,
        dot x (dot y z) =  dot (dot x y) z;
    unit_left:
      forall x:A,
        dot one x = x;
    unit_right:
      forall x:A,
        dot x one = x }.
  Check Compose.comp.
  Check Compose.id.
  Instance Monoid_add_0: Monoid add 0.
  Proof.
    split.
    - intros. apply PeanoNat.Nat.add_assoc.
    - intros. apply PeanoNat.Nat.add_0_l.
    - intros. apply PeanoNat.Nat.add_0_r.
  Qed.
  Print Monoid_add_0.
  

End Monoid.
