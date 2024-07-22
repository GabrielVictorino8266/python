first_score = float(input("Informe seu primeiro score: "))
second_score = float(input("Informe seu segundo score: "))
final_score = (first_score + second_score) / 2

situation = "Reprovado" if final_score < 5.0 else "Recuperação" if final_score > 5.0 and final_score < 6.9 else "Aprovado"

print(f"Após calcular sua média, sua nota final será: {final_score} e você estará {situation}")