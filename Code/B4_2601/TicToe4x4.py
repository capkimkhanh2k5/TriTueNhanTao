import tkinter as tk
from tkinter import messagebox
import math
import time

class TicTacToe4x4GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe 4x4 - Alpha-Beta vs Minimax")
        self.window.geometry("+200+50")
        self.window.resizable(False, False)
        
        self.board = [' ' for _ in range(16)]  # 4x4 = 16 ô
        self.human = 'X'
        self.ai = 'O'
        self.current_player = self.human
        self.game_over = False
        
        # Giới hạn độ sâu tìm kiếm
        self.MAX_DEPTH = 4
        
        # Thống kê so sánh
        self.alphabeta_nodes = 0
        self.minimax_nodes = 0
        self.alphabeta_time = 0
        self.minimax_time = 0
        self.move_count = 0
        self.alphabeta_cutoffs = 0
        
        # Tạo frame chính
        main_frame = tk.Frame(self.window, bg='#2c3e50')
        main_frame.pack(padx=20, pady=20)
        
        # Tiêu đề
        title_label = tk.Label(
            main_frame, 
            text="TIC-TAC-TOE 4x4\nAlpha-Beta AI", 
            font=('Arial', 18, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 5))
        
        # Khung cấu hình độ sâu
        config_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RIDGE, bd=2)
        config_frame.grid(row=1, column=0, columnspan=4, pady=(0, 5), padx=5, sticky='ew')
        
        depth_label = tk.Label(
            config_frame,
            text=f"Độ sâu tìm kiếm: {self.MAX_DEPTH}",
            font=('Arial', 10, 'bold'),
            bg='#34495e',
            fg='#f39c12'
        )
        depth_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Slider để điều chỉnh độ sâu
        self.depth_slider = tk.Scale(
            config_frame,
            from_=3,
            to=8,
            orient=tk.HORIZONTAL,
            bg='#34495e',
            fg='white',
            highlightthickness=0,
            command=lambda v: self.update_depth(int(v), depth_label)
        )
        self.depth_slider.set(self.MAX_DEPTH)
        self.depth_slider.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Khung thống kê
        stats_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RIDGE, bd=2)
        stats_frame.grid(row=2, column=0, columnspan=4, pady=(0, 10), padx=5, sticky='ew')
        
        # Nhãn thống kê Alpha-Beta
        self.ab_label = tk.Label(
            stats_frame,
            text="Alpha-Beta: 0 nodes | 0 cutoffs | 0.00s",
            font=('Arial', 9, 'bold'),
            bg='#34495e',
            fg='#2ecc71'
        )
        self.ab_label.pack(pady=2)
        
        # Nhãn thống kê Minimax
        self.mm_label = tk.Label(
            stats_frame,
            text="Minimax: 0 nodes | 0.00s",
            font=('Arial', 9),
            bg='#34495e',
            fg='#95a5a6'
        )
        self.mm_label.pack(pady=2)
        
        # Nhãn hiệu suất
        self.perf_label = tk.Label(
            stats_frame,
            text="Tiết kiệm: 0%",
            font=('Arial', 9, 'bold'),
            bg='#34495e',
            fg='#e67e22'
        )
        self.perf_label.pack(pady=2)
        
        # Nhãn trạng thái
        self.status_label = tk.Label(
            main_frame,
            text="Lượt của bạn (X)",
            font=('Arial', 12),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        self.status_label.grid(row=3, column=0, columnspan=4, pady=(5, 10))
        
        # Tạo các nút cho bảng game 4x4
        self.buttons = []
        for i in range(16):
            btn = tk.Button(
                main_frame,
                text='',
                font=('Arial', 28, 'bold'),
                width=3,
                height=1,
                bg='#34495e',
                fg='white',
                activebackground='#475a6e',
                command=lambda pos=i: self.human_move(pos)
            )
            row = (i // 4) + 4
            col = i % 4
            btn.grid(row=row, column=col, padx=3, pady=3)
            self.buttons.append(btn)
        
        # Nút chơi lại
        reset_btn = tk.Button(
            main_frame,
            text='Chơi lại',
            font=('Arial', 11),
            bg='#27ae60',
            fg='white',
            activebackground='#229954',
            command=self.reset_game,
            padx=20,
            pady=8
        )
        reset_btn.grid(row=8, column=0, columnspan=4, pady=(10, 0))
        
        print("\n" + "="*70)
        print("GAME TIC-TAC-TOE 4x4 - SO SÁNH ALPHA-BETA vs MINIMAX")
        print("="*70)
        print(f"Độ sâu tìm kiếm: {self.MAX_DEPTH}")
        print("Điều kiện thắng: 4 ô liên tiếp (ngang/dọc/chéo)")
        print("Thuật toán chính (chơi với bạn): Alpha-Beta Pruning")
        print("Thuật toán chạy ngầm (so sánh): Minimax")
        print("="*70 + "\n")
    
    def update_depth(self, value, label):
        """Cập nhật giá trị độ sâu"""
        if not self.game_over and all(cell == ' ' for cell in self.board):
            self.MAX_DEPTH = value
            label.config(text=f"Độ sâu tìm kiếm: {self.MAX_DEPTH}")
    
    def human_move(self, position):
        """Xử lý nước đi của người chơi"""
        if self.game_over or self.board[position] != ' ':
            return
        
        self.make_move(position, self.human)
        self.buttons[position].config(text=self.human, fg='#3498db')
        self.move_count += 1
        
        print(f"\n{'='*70}")
        print(f"NƯỚC ĐI #{self.move_count} - Người chơi đánh vào ô {position + 1}")
        print(f"{'='*70}")
        
        if self.check_winner(self.human):
            self.game_over = True
            self.status_label.config(text="Bạn thắng! 🎉")
            print("\n🎉 KẾT QUẢ: Người chơi THẮNG!\n")
            messagebox.showinfo("Kết thúc", "Chúc mừng! Bạn đã thắng!")
            return
        
        if not self.available_moves():
            self.game_over = True
            self.status_label.config(text="Hòa!")
            print("\n🤝 KẾT QUẢ: Trận đấu HÒA!\n")
            messagebox.showinfo("Kết thúc", "Trận đấu hòa!")
            return
        
        self.status_label.config(text="AI đang suy nghĩ...")
        self.window.update()
        self.window.after(300, self.ai_move)
    
    def ai_move(self):
        """Xử lý nước đi của AI - so sánh 2 thuật toán"""
        if self.game_over:
            return
        
        self.move_count += 1
        print(f"\n{'='*70}")
        print(f"NƯỚC ĐI #{self.move_count} - AI đang tính toán (Max depth: {self.MAX_DEPTH})...")
        print(f"{'='*70}")
        
        # Chạy Alpha-Beta (thuật toán chính)
        self.alphabeta_nodes = 0
        self.alphabeta_cutoffs = 0
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
        
        # Hiển thị kết quả so sánh
        print(f"\n┌─ ALPHA-BETA PRUNING (Thuật toán chính)")
        print(f"│  ├─ Nước đi: Ô {best_move + 1}")
        print(f"│  ├─ Điểm số: {ab_score}")
        print(f"│  ├─ Nodes duyệt: {self.alphabeta_nodes}")
        print(f"│  ├─ Cutoffs: {self.alphabeta_cutoffs}")
        print(f"│  └─ Thời gian: {self.alphabeta_time*1000:.2f}ms")
        print(f"│")
        print(f"└─ MINIMAX (Chạy ngầm để so sánh)")
        print(f"   ├─ Nước đi: Ô {mm_move + 1}")
        print(f"   ├─ Điểm số: {mm_score}")
        print(f"   ├─ Nodes duyệt: {self.minimax_nodes}")
        print(f"   └─ Thời gian: {self.minimax_time*1000:.2f}ms")
        
        # Tính toán hiệu suất
        if self.minimax_nodes > 0:
            saving = ((self.minimax_nodes - self.alphabeta_nodes) / self.minimax_nodes) * 100
            speedup = self.minimax_time / self.alphabeta_time if self.alphabeta_time > 0 else 1
            print(f"\n📊 HIỆU SUẤT:")
            print(f"   ├─ Tiết kiệm nodes: {saving:.1f}% ({self.minimax_nodes - self.alphabeta_nodes} nodes)")
            print(f"   ├─ Nhanh hơn: {speedup:.2f}x")
            print(f"   └─ Kết quả giống nhau: {'✓ CÓ' if ab_score == mm_score else '✗ KHÔNG'}")
        
        # Cập nhật giao diện
        self.update_stats_display()
        
        # Thực hiện nước đi
        self.make_move(best_move, self.ai)
        self.buttons[best_move].config(text=self.ai, fg='#e74c3c')
        
        print(f"\nAI đánh vào ô {best_move + 1}")
        
        if self.check_winner(self.ai):
            self.game_over = True
            self.status_label.config(text="AI thắng!")
            print("\n🤖 KẾT QUẢ: AI THẮNG!\n")
            messagebox.showinfo("Kết thúc", "AI đã thắng!")
            return
        
        if not self.available_moves():
            self.game_over = True
            self.status_label.config(text="Hòa!")
            print("\n🤝 KẾT QUẢ: Trận đấu HÒA!\n")
            messagebox.showinfo("Kết thúc", "Trận đấu hòa!")
            return
        
        self.status_label.config(text="Lượt của bạn (X)")
    
    def evaluate_board(self):
        """Đánh giá trạng thái bảng khi đạt giới hạn độ sâu"""
        score = 0
        
        # Kiểm tra tất cả các hàng, cột, chéo có tiềm năng
        lines = []
        
        # Hàng ngang
        for i in range(4):
            for j in range(1):  # 4 cách tạo 4 ô liên tiếp
                lines.append([i*4+j, i*4+j+1, i*4+j+2, i*4+j+3])
        
        # Hàng dọc
        for i in range(4):
            for j in range(1):
                lines.append([i+j*4, i+(j+1)*4, i+(j+2)*4, i+(j+3)*4])
        
        # Chéo chính
        for i in range(1):
            for j in range(1):
                lines.append([i*4+j, (i+1)*4+j+1, (i+2)*4+j+2, (i+3)*4+j+3])
        
        # Chéo phụ
        for i in range(1):
            for j in range(3, 4):
                lines.append([i*4+j, (i+1)*4+j-1, (i+2)*4+j-2, (i+3)*4+j-3])
        
        for line in lines:
            ai_count = sum(1 for pos in line if self.board[pos] == self.ai)
            human_count = sum(1 for pos in line if self.board[pos] == self.human)
            
            if ai_count > 0 and human_count == 0:
                score += ai_count ** 2
            elif human_count > 0 and ai_count == 0:
                score -= human_count ** 2
        
        return score
    
    def minimax(self, depth, maximizing_player):
        """Thuật toán Minimax với giới hạn độ sâu"""
        self.minimax_nodes += 1
        
        if self.check_winner(self.ai):
            return {'score': 1000 - depth, 'position': None}
        if self.check_winner(self.human):
            return {'score': depth - 1000, 'position': None}
        if not self.available_moves():
            return {'score': 0, 'position': None}
        
        # Giới hạn độ sâu - đánh giá heuristic
        if depth >= self.MAX_DEPTH:
            return {'score': self.evaluate_board(), 'position': None}
        
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
        """Thuật toán Alpha-Beta Pruning với giới hạn độ sâu"""
        self.alphabeta_nodes += 1
        
        if self.check_winner(self.ai):
            return {'score': 1000 - depth, 'position': None}
        if self.check_winner(self.human):
            return {'score': depth - 1000, 'position': None}
        if not self.available_moves():
            return {'score': 0, 'position': None}
        
        # Giới hạn độ sâu - đánh giá heuristic
        if depth >= self.MAX_DEPTH:
            return {'score': self.evaluate_board(), 'position': None}
        
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
                    self.alphabeta_cutoffs += 1
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
                    self.alphabeta_cutoffs += 1
                    break  # Alpha cutoff
            return {'score': min_eval, 'position': best_move}
    
    def update_stats_display(self):
        """Cập nhật hiển thị thống kê trên GUI"""
        self.ab_label.config(text=f"Alpha-Beta: {self.alphabeta_nodes} nodes | {self.alphabeta_cutoffs} cutoffs | {self.alphabeta_time*1000:.2f}ms")
        self.mm_label.config(text=f"Minimax: {self.minimax_nodes} nodes | {self.minimax_time*1000:.2f}ms")
        
        if self.minimax_nodes > 0:
            saving = ((self.minimax_nodes - self.alphabeta_nodes) / self.minimax_nodes) * 100
            self.perf_label.config(text=f"Tiết kiệm: {saving:.1f}%")
    
    def available_moves(self):
        """Trả về danh sách các ô còn trống"""
        return [i for i, x in enumerate(self.board) if x == ' ']
    
    def make_move(self, position, player):
        """Thực hiện nước đi"""
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False
    
    def check_winner(self, player):
        """Kiểm tra người chơi có thắng không (4 ô liên tiếp)"""
        # Hàng ngang (4 ô liên tiếp)
        for i in range(4):
            for j in range(1):  # 4-3 = 1 cách
                if all(self.board[i*4+j+k] == player for k in range(4)):
                    return True
        
        # Hàng dọc (4 ô liên tiếp)
        for i in range(4):
            for j in range(1):
                if all(self.board[i+(j+k)*4] == player for k in range(4)):
                    return True
        
        # Đường chéo chính (4 ô liên tiếp)
        for i in range(1):
            for j in range(1):
                if all(self.board[(i+k)*4+j+k] == player for k in range(4)):
                    return True
        
        # Đường chéo phụ (4 ô liên tiếp)
        for i in range(1):
            for j in range(3, 4):
                if all(self.board[(i+k)*4+j-k] == player for k in range(4)):
                    return True
        
        return False
    
    def reset_game(self):
        """Khởi động lại game"""
        self.board = [' ' for _ in range(16)]
        self.game_over = False
        self.alphabeta_nodes = 0
        self.minimax_nodes = 0
        self.alphabeta_time = 0
        self.minimax_time = 0
        self.alphabeta_cutoffs = 0
        self.move_count = 0
        self.status_label.config(text="Lượt của bạn (X)")
        self.ab_label.config(text="Alpha-Beta: 0 nodes | 0 cutoffs | 0.00s")
        self.mm_label.config(text="Minimax: 0 nodes | 0.00s")
        self.perf_label.config(text="Tiết kiệm: 0%")
        
        for btn in self.buttons:
            btn.config(text='', state='normal')
        
        print("\n" + "="*70)
        print("GAME MỚI BẮT ĐẦU")
        print(f"Độ sâu tìm kiếm: {self.MAX_DEPTH}")
        print("="*70 + "\n")
    
    def run(self):
        """Chạy game"""
        self.window.mainloop()

# Chạy game
if __name__ == "__main__":
    game = TicTacToe4x4GUI()
    game.run()