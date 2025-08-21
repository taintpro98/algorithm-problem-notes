use serde::{Deserialize, Serialize};
use std::fs;
use std::io;

#[derive(Serialize, Deserialize)]
struct Todo {
    tasks: Vec<String>,
}

impl Todo {
    fn new() -> Todo {
        Todo { tasks: Vec::new() }
    }

    fn add_task(&mut self, task: String) {
        self.tasks.push(task);
    }

    fn list_tasks(&self) {
        if self.tasks.is_empty() {
            println!("Danh sách công việc trống!");
        } else {
            for (index, task) in self.tasks.iter().enumerate() {
                println!("{}: {}", index + 1, task);
            }
        }
    }

    fn remove_task(&mut self, index: usize) -> Result<(), String> {
        if index == 0 || index > self.tasks.len() {
            return Err(String::from("Chỉ số không hợp lệ!"));
        }
        self.tasks.remove(index - 1);
        Ok(())
    }

    fn save_to_file(&self, filename: &str) -> Result<(), io::Error> {
        let json = serde_json::to_string_pretty(&self)?;
        fs::write(filename, json)?;
        Ok(())
    }

    fn load_from_file(filename: &str) -> Result<Todo, io::Error> {
        let contents = fs::read_to_string(filename)?;
        let todo: Todo = serde_json::from_str(&contents)?;
        Ok(todo)
    }
}

fn main() {
    let filename = "todo.json";
    let mut todo = match Todo::load_from_file(filename) {
        Ok(todo) => todo,
        Err(_) => Todo::new(),
    };

    loop {
        println!("\n=== Quản lý danh sách công việc ===");
        println!("1. Thêm công việc");
        println!("2. Liệt kê công việc");
        println!("3. Xóa công việc");
        println!("4. Thoát");
        println!("Chọn một tùy chọn (1-4): ");

        let mut choice = String::new();
        io::stdin()
            .read_line(&mut choice)
            .expect("Lỗi khi đọc đầu vào");

        let choice: u32 = match choice.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Vui lòng nhập số hợp lệ!");
                continue;
            }
        };

        match choice {
            1 => {
                println!("Nhập công việc mới: ");
                let mut task = String::new();
                io::stdin()
                    .read_line(&mut task)
                    .expect("Lỗi khi đọc đầu vào");
                let task = task.trim().to_string();
                if !task.is_empty() {
                    todo.add_task(task);
                    if let Err(e) = todo.save_to_file(filename) {
                        println!("Lỗi khi lưu file: {}", e);
                    } else {
                        println!("Đã thêm công việc!");
                    }
                } else {
                    println!("Công việc không được để trống!");
                }
            }
            2 => {
                todo.list_tasks();
            }
            3 => {
                println!("Nhập chỉ số công việc cần xóa: ");
                let mut index = String::new();
                io::stdin()
                    .read_line(&mut index)
                    .expect("Lỗi khi đọc đầu vào");
                let index: usize = match index.trim().parse() {
                    Ok(num) => num,
                    Err(_) => {
                        println!("Vui lòng nhập số hợp lệ!");
                        continue;
                    }
                };
                match todo.remove_task(index) {
                    Ok(_) => {
                        if let Err(e) = todo.save_to_file(filename) {
                            println!("Lỗi khi lưu file: {}", e);
                        } else {
                            println!("Đã xóa công việc!");
                        }
                    }
                    Err(e) => println!("Lỗi: {}", e),
                }
            }
            4 => {
                println!("Tạm biệt!");
                break;
            }
            _ => println!("Tùy chọn không hợp lệ!"),
        }
    }
}