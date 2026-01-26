import tkinter as tk
from tkinter import messagebox
import math
import time

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe - Alpha-Beta vs Minimax")
        self.window.geometry("+300+100")
        self.window.resizable(False, False)
        
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.ai = 'O'
        self.current_player = self.human
        self.game_over = False
        
        # Thống kê so sánh
        self.alphabeta_nodes = 0
        self.minimax_nodes = 0
        self.alphabeta_time = 0
        self.minimax_time = 0
        self.move_count = 0
        
        # Tạo frame chính
        main_frame = tk.Frame(self.window, bg='#2c3e50')
        main_frame.pack(padx=20, pady=20)
        
        # Tiêu đề
        title_label = tk.Label(
            main_frame, 
            text="TIC-TAC-TOE\nAlpha-Beta AI", 
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 5))
        
        # Khung thống kê
        stats_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RIDGE, bd=2)
        stats_frame.grid(row=1, column=0, columnspan=3, pady=(0, 10), padx=5, sticky='ew')
        
        # Nhan thong ke Alpha-Beta
        self.ab_label = tk.Label(
            stats_frame,
            text="Alpha-Beta: 0 nodes | 0.00s",
            font=('Arial', 10, 'bold'),
            bg='#34495e',
            fg='#2ecc71'
        )
        self.ab_label.pack(pady=2)
        
        # Nhan thong ke Minimax
        self.mm_label = tk.Label(
            stats_frame,
            text="Minimax: 0 nodes | 0.00s",
            font=('Arial', 10),
            bg='#34495e',
            fg='#95a5a6'
        )
        self.mm_label.pack(pady=2)
        
        # Nhan hieu suat
        self.perf_label = tk.Label(
            stats_frame,
            text="Tiet kiem: 0%",
            font=('Arial', 10, 'bold'),
            bg='#34495e',
            fg='#e67e22'
        )
        self.perf_label.pack(pady=2)
        
        # Nhan trang thai
        self.status_label = tk.Label(
            main_frame,
            text="Luot cua ban (X)",
            font=('Arial', 13),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        self.status_label.grid(row=2, column=0, columnspan=3, pady=(5, 10))
        
        # Tao cac nut cho bang game
        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                main_frame,
                text='',
                font=('Arial', 36, 'bold'),
                width=4,
                height=2,
                bg='#34495e',
                fg='white',
                activebackground='#475a6e',
                command=lambda pos=i: self.human_move(pos)
            )
            row = (i // 3) + 3
            col = i % 3
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)
        
        # Nut choi lai
        reset_btn = tk.Button(
            main_frame,
            text='Choi lai',
            font=('Arial', 12),
            bg='#27ae60',
            fg='white',
            activebackground='#229954',
            command=self.reset_game,
            padx=20,
            pady=8
        )
        reset_btn.grid(row=6, column=0, columnspan=3, pady=(10, 0))
        
        print("\n" + "="*70)
        print("GAME TIC-TAC-TOE - SO SANH ALPHA-BETA vs MINIMAX")
        print("="*70)
        print("Thuat toan chinh (choi voi ban): Alpha-Beta Pruning")
        print("Thuat toan chay ngam (so sanh): Minimax")
        print("="*70 + "\n")
        
    def human_move(self, position):
        """Xu ly nuoc di cua nguoi choi"""
        if self.game_over or self.board[position] != ' ':
            return
        
        self.make_move(position, self.human)
        self.buttons[position].config(text=self.human, fg='#3498db')
        self.move_count += 1
        
        print(f"\n{'='*70}")
        print(f"NUOC DI #{self.move_count} - Nguoi choi danh vao o {position + 1}")
        print(f"{'='*70}")
        
        if self.check_winner(self.human):
            self.game_over = True
            self.status_label.config(text="Ban thang! 🎉")
            print("\n🎉 KET QUA: Nguoi choi THANG!\n")
            messagebox.showinfo("Ket thuc", "Chuc mung! Ban da thang!")
            return
        
        if not self.available_moves():
            self.game_over = True
            self.status_label.config(text="Hoa!")
            print("\n🤝 KET QUA: Tran dau HOA!\n")
            messagebox.showinfo("Ket thuc", "Tran dau hoa!")
            return
        
        self.status_label.config(text="AI dang suy nghi...")
        self.window.update()
        self.window.after(300, self.ai_move)
    
    def ai_move(self):
        """Xu ly nuoc di cua AI - so sanh 2 thuat toan"""
        if self.game_over:
            return
        
        self.move_count += 1
        print(f"\n{'='*70}")
        print(f"NUOC DI #{self.move_count} - AI dang tinh toan...")
        print(f"{'='*70}")
        
        # Chạy Alpha-Beta (thuật toán chính)
        self.alphabeta_nodes = 0
        start_time = time.time()
        ab_result = self.alphabeta(0, True, -math.inf, math.inf)
        self.alphabeta_time = time.time() - start_time
        best_move = ab_result['position']
        ab_score = ab_result['score']
        
        # Chạy Minimax ngầm để so sánh
        self.minimax_nodes = 0
        start_time = time.time()
        mm_result = self.minimax(0, True)
        self.minimax_time = time.time() - start_time
        mm_score = mm_result['score']
        mm_move = mm_result['position']
        
        # Hien thi ket qua so sanh
        print(f"\n┌─ ALPHA-BETA PRUNING (Thuat toan chinh)")
        print(f"│  ├─ Nuoc di: O {best_move + 1}")
        print(f"│  ├─ Diem so: {ab_score}")
        print(f"│  ├─ Nodes duyet: {self.alphabeta_nodes}")
        print(f"│  └─ Thoi gian: {self.alphabeta_time*1000:.2f}ms")
        print(f"│")
        print(f"└─ MINIMAX (Chay ngam de so sanh)")
        print(f"   ├─ Nuoc di: O {mm_move + 1}")
        print(f"   ├─ Diem so: {mm_score}")
        print(f"   ├─ Nodes duyet: {self.minimax_nodes}")
        print(f"   └─ Thoi gian: {self.minimax_time*1000:.2f}ms")
        
        # Tinh toan hieu suat
        if self.minimax_nodes > 0:
            saving = ((self.minimax_nodes - self.alphabeta_nodes) / self.minimax_nodes) * 100
            speedup = self.minimax_time / self.alphabeta_time if self.alphabeta_time > 0 else 1
            print(f"\n📊 HIEU SUAT:")
            print(f"   ├─ Tiet kiem nodes: {saving:.1f}% ({self.minimax_nodes - self.alphabeta_nodes} nodes)")
            print(f"   ├─ Nhanh hon: {speedup:.2f}x")
            print(f"   └─ Ket qua giong nhau: {'✓ CO' if ab_score == mm_score else '✗ KHONG'}")
        
        # Cap nhat giao dien
        self.update_stats_display()
        
        # Thuc hien nuoc di
        self.make_move(best_move, self.ai)
        self.buttons[best_move].config(text=self.ai, fg='#e74c3c')
        
        print(f"\nAI danh vao o {best_move + 1}")
        
        if self.check_winner(self.ai):
            self.game_over = True
            self.status_label.config(text="AI thang!")
            print("\n🤖 KET QUA: AI THANG!\n")
            messagebox.showinfo("Ket thuc", "AI da thang!")
            return
        
        if not self.available_moves():
            self.game_over = True
            self.status_label.config(text="Hoa!")
            print("\n🤝 KET QUA: Tran dau HOA!\n")
            messagebox.showinfo("Ket thuc", "Tran dau hoa!")
            return
        
        self.status_label.config(text="Luot cua ban (X)")
    
    def minimax(self, depth, maximizing_player):
        """Thuat toan Minimax - chay ngam de so sanh"""
        self.minimax_nodes += 1
        
        if self.check_winner(self.ai):
            return {'score': 10 - depth, 'position': None}
        if self.check_winner(self.human):
            return {'score': depth - 10, 'position': None}
        if not self.available_moves():
            return {'score': 0, 'position': None}
        
        if maximizing_player:
            max_eval = -math.inf
            best_move = None
            for move in self.available_moves():
                self.board[move] = self.ai
                eval_result = self.minimax(depth + 1, False)
                self.board[move] = ' '
                if eval_result['score'] > max_eval:
                    max_eval = eval_result['score']
                    best_move = move
            return {'score': max_eval, 'position': best_move}
        else:
            min_eval = math.inf
            best_move = None
            for move in self.available_moves():
                self.board[move] = self.human
                eval_result = self.minimax(depth + 1, True)
                self.board[move] = ' '
                if eval_result['score'] < min_eval:
                    min_eval = eval_result['score']
                    best_move = move
            return {'score': min_eval, 'position': best_move}
    
    def alphabeta(self, depth, maximizing_player, alpha, beta):
        """Thuat toan Alpha-Beta Pruning - choi voi nguoi"""
        self.alphabeta_nodes += 1
        
        if self.check_winner(self.ai):
            return {'score': 10 - depth, 'position': None}
        if self.check_winner(self.human):
            return {'score': depth - 10, 'position': None}
        if not self.available_moves():
            return {'score': 0, 'position': None}
        
        if maximizing_player:
            max_eval = -math.inf
            best_move = None
            for move in self.available_moves():
                self.board[move] = self.ai
                eval_result = self.alphabeta(depth + 1, False, alpha, beta)
                self.board[move] = ' '
                if eval_result['score'] > max_eval:
                    max_eval = eval_result['score']
                    best_move = move
                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break  # Beta cutoff
            return {'score': max_eval, 'position': best_move}
        else:
            min_eval = math.inf
            best_move = None
            for move in self.available_moves():
                self.board[move] = self.human
                eval_result = self.alphabeta(depth + 1, True, alpha, beta)
                self.board[move] = ' '
                if eval_result['score'] < min_eval:
                    min_eval = eval_result['score']
                    best_move = move
                beta = min(beta, min_eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            return {'score': min_eval, 'position': best_move}
    
    def update_stats_display(self):
        """Cap nhat hien thi thong ke tren GUI"""
        self.ab_label.config(text=f"Alpha-Beta: {self.alphabeta_nodes} nodes | {self.alphabeta_time*1000:.2f}ms")
        self.mm_label.config(text=f"Minimax: {self.minimax_nodes} nodes | {self.minimax_time*1000:.2f}ms")
        
        if self.minimax_nodes > 0:
            saving = ((self.minimax_nodes - self.alphabeta_nodes) / self.minimax_nodes) * 100
            self.perf_label.config(text=f"Tiet kiem: {saving:.1f}%")
    
    def print_board_console(self):
        """In bang ra console"""
        pass
    
    def available_moves(self):
        """Tra ve danh sach cac o con trong"""
        return [i for i, x in enumerate(self.board) if x == ' ']
    
    def make_move(self, position, player):
        """Thuc hien nuoc di"""
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False
    
    def check_winner(self, player):
        """Kiem tra nguoi choi co thang khong"""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # hang ngang
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # hang doc
            [0, 4, 8], [2, 4, 6]              # duong cheo
        ]
        
        for condition in win_conditions:
            if (self.board[condition[0]] == player and
                self.board[condition[1]] == player and
                self.board[condition[2]] == player):
                return True
        return False
    
    def reset_game(self):
        """Khoi dong lai game"""
        self.board = [' ' for _ in range(9)]
        self.game_over = False
        self.alphabeta_nodes = 0
        self.minimax_nodes = 0
        self.alphabeta_time = 0
        self.minimax_time = 0
        self.move_count = 0
        self.status_label.config(text="Luot cua ban (X)")
        self.ab_label.config(text="Alpha-Beta: 0 nodes | 0.00s")
        self.mm_label.config(text="Minimax: 0 nodes | 0.00s")
        self.perf_label.config(text="Tiet kiem: 0%")
        
        for btn in self.buttons:
            btn.config(text='', state='normal')
        
        print("\n" + "="*70)
        print("GAME MOI BAT DAU")
        print("="*70 + "\n")
    
    def run(self):
        """Chay game"""
        self.window.mainloop()

# Chạy game
if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()