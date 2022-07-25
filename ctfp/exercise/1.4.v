Require Import List.
Module Compose.
  Definition id {A}  := fun a: A => a.
  Definition comp_1 {A B C: Type} {x: A} (g: B->C) (f: A->B) := g (f x).
  Check comp_1.                 (* final typle is C *)
  Definition comp {A B C: Type} (g: B->C) (f: A->B)  := 
    fun x : A => g (f x).
  Check comp.
  Notation "f [] g" := (comp f g) (at level 30).


  Lemma id_identity {A B}:
    forall f : A->B, f [] id = f.
  Proof.
    intros.
    unfold comp.
    unfold id.
    reflexivity.
  Qed.

  Lemma id_commu {A B}:
    forall f : A->B, f [] id = id [] f.
  Proof.
    intros.
    unfold comp.
    simpl.
    unfold id.
    reflexivity.
  Qed.

  Lemma comp_assoc {A B C D}:
    forall (f: A->B) (g: B->C) (h: C->D),
      h [] g [] f = h [] (g [] f).
  Proof.
    intros.
    unfold comp.
    reflexivity.
  Qed.

End Compose.
