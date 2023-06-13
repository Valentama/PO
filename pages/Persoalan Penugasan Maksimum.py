import streamlit as st
import numpy as np
from scipy.optimize import linear_sum_assignment

def maximum_assignment(cost_matrix):
    #rumus
    row_ind, col_ind = linear_sum_assignment(cost_matrix, maximize=True)
    total_cost = cost_matrix[row_ind, col_ind].sum()
    assignments = [(row, col) for row, col in zip(row_ind, col_ind)]
    return assignments, total_cost

def main():
    st.title("Persoalan Penugasan Maksimum")
    #input pekerja & tugas
    p = st.number_input("Jumlah pekerja", min_value=1, value=1, step=1)
    t = st.number_input("Jumlah tugas", min_value=1, value=1, step=1)
    
    cost_matrix = np.zeros((p, t))
    st.write('Jika pekerja tidak bisa melakukan tugas tertentu isi dengan biaya terkecil/0')
    for bp in range(p):
        for bt in range(t):
            #input biaya
            cost_matrix[bp, bt] = st.number_input(f"Biaya Pekerja {bp+1} Tugas {bt+1}")
    
    if st.button("Hitung"):
        assignments, total_cost = maximum_assignment(cost_matrix)
        st.write("Hasil Penugasan Maksimum:")
        st.write("Biaya Optimum:", total_cost)
        st.write("Pasangan Tugas-Pekerja:")
        for assignment in assignments:
            st.write(f"Tugas {assignment[1]+1} dikerjakan oleh Pekerja {assignment[0]+1}")

if __name__ == "__main__":
    main()
