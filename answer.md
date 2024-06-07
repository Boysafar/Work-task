**1-task**
 Explain the different types of JOINs in SQL and provide an example for each.
  INNER JOIN faqat ikkala jadvaldagi mos keladigan yozuvlarni qaytaradi. 
*      SELECT employees.name, departments.department_name
       FROM employees
       INNER JOIN departments ON employees.department_id = departments.id;

  LEFT JOIN chap (birinchi) jadvaldagi barcha yozuvlarni va o'ng (ikkinchi) jadvaldagi mos keladigan yozuvlarni qaytaradi
  Agar mos yozuv topilmasa, o'ng jadvaldagi ustunlar uchun NULL qiymat qaytariladi.
*       SELECT employees.name, departments.department_name
       FROM employees
       LEFT JOIN departments ON employees.department_id = departments.id;

  RIGHT JOIN o'ng (ikkinchi) jadvaldagi barcha yozuvlarni va chap (birinchi) jadvaldagi mos keladigan yozuvlarni qaytaradi. 
  Agar mos yozuv topilmasa, chap jadvaldagi ustunlar uchun NULL qiymat qaytariladi. 
*       SELECT employees.name, departments.department_name
       FROM employees
       RIGHT JOIN departments ON employees.department_id = departments.id;

  FULL JOIN ikkala jadvaldagi barcha yozuvlarni qaytaradi. Agar bir jadvadda mos yozuv topilmasa,
  tegishli ustunlar uchun NULL qiymat qaytariladi.
*       SELECT employees.name, departments.department_name
        FROM employees
        FULL JOIN departments ON employees.department_id = departments.id;





**2-task**
 Describe the ALTER TABLE statement and provide examples of how to add a column, modify a column, and drop a column.
  SQL-da ALTER TABLE bayonoti jadval tuzilmasini o'zgartirish uchun ishlatiladi.
  Bu bayonot yordamida jadvalga yangi ustunlar qo'shish, mavjud ustunlarni o'zgartirish yoki olib tashlash mumkin
*
     Jadvalga yangi ustun qo'shish uchun ADD kalit so'zidan foydalaniladi.
*       ALTER TABLE table_name ADD column_name data_type;

     Ustunni o'zgartirish uchun ALTER COLUMN kalit so'zidan foydalaniladi.
     Bu ustunning ma'lumot turini, nomini yoki boshqa xususiyatlarini o'zgartirish imkonini beradi.
*       ALTER TABLE table_name ALTER COLUMN column_name SET DATA TYPE new_data_type;

     Ustunni olib tashlash uchun DROP COLUMN kalit so'zidan foydalaniladi.
*       ALTER TABLE table_name DROP COLUMN column_name;




**3-task**
    Foreign key (chet el kaliti) ma'lumotlar bazasidagi jadval (table) orasidagi munosabatlarni ifodalash uchun ishlatiladi. 
    Foreign key bir jadvaldagi ustunni (yoki ustunlar guruhini) boshqa jadvaldagi ustun (yoki ustunlar guruhi) bilan bog'laydi. 
    Bu munosabat ma'lumotlar integritetini saqlashga yordam beradi, ya'ni ma'lumotlar bazasidagi bog'liqlik va qoidalarni ta'minlaydi.

        Misol: Orders jadvalidagi CustomerID ustunini Customers jadvalidagi CustomerID ustuniga foreign key sifatida bog'lash:
        CREATE TABLE Customers (
            CustomerID INT PRIMARY KEY,
            CustomerName VARCHAR(100)
        );

        CREATE TABLE Orders (
            OrderID INT PRIMARY KEY,
            OrderDate DATE,
            CustomerID INT,
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
        );

        ON DELETE CASCADE: Agar asosiy jadvaldagi yozuv o'chirilsa, bog'liq yozuvlar ham avtomatik ravishda o'chiriladi.
        ON UPDATE CASCADE: Agar asosiy jadvaldagi yozuv yangilansa, bog'liq yozuvlar ham avtomatik ravishda yangilanadi.
        Misol: ON DELETE CASCADE va ON UPDATE CASCADE bilan foreign key yaratish:
        CREATE TABLE Orders (
            OrderID INT PRIMARY KEY,
            OrderDate DATE,
            CustomerID INT,
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        );




**4-task**
    Explain the full flow of how a request is processed in a Django application,
    starting from when a user makes a request to when a response is sent back.
   1. URL So'rovi
      Foydalanuvchi brauzer orqali URL manzilga so'rov yuboradi. Bu so'rov HTTP protokoli yordamida serverga yetib boradi.
        
   2. Django Middleware
      So'rov serverga yetib borgandan so'ng, u Django dasturi ichida middleware qatlamidan o'tadi. 
      Middleware — bu so'rov va javobni qayta ishlashda ishlatiladigan komponentlar to'plami bo'lib, 
      ular turli vazifalarni bajaradi, masalan, autentifikatsiya, keshlash, xavfsizlik tekshiruvi va boshqalar.
        
      Middleware Ishlash Tartibi:
          process_request(request): So'rovga ishlov berishdan oldin chaqiriladi.
          process_view(request, view_func, view_args, view_kwargs): View funksiyasi chaqirilishidan oldin chaqiriladi.
          process_exception(request, exception): View funktsiyasi istisno tashlagan bo'lsa, chaqiriladi.
          process_template_response(request, response): Javobni shablon bilan birlashtirishdan oldin chaqiriladi.
          process_response(request, response): Javobni qaytarishdan oldin chaqiriladi.

   3. URL Routing
      Django so'rovni qabul qilgach, URL routing (yo'naltirish) jarayoniga o'tadi. 
      Django urls.py faylidagi URL yo'llarini tekshirib, so'rov qaysi view funksiyasiga mos kelishini aniqlaydi.

   4. View Funksiyasi
      URL routing orqali mos keluvchi view funksiyasi aniqlangach, Django ushbu view funksiyasini chaqiradi. 
      View funksiya so'rovni qabul qilib, kerakli logikani bajaradi. 
      U odatda model bilan ishlaydi, kerakli ma'lumotlarni olib, shablonni render qilish uchun kontekstni tayyorlaydi.

   5. Model (Ma'lumotlar Bazasi)
      Agar view funksiyasi ma'lumotlar bazasidan ma'lumot olishi kerak bo'lsa, u modeldan foydalanadi. 
      Django ORM (Object-Relational Mapping) orqali ma'lumotlar bazasiga so'rov yuboriladi va natijalar qaytariladi.

   6. Shablon (Template) Render Qilish
      View funksiya kerakli ma'lumotlarni to'plab bo'lgach, u ma'lumotlarni shablon bilan birlashtirib, HTML javob hosil qiladi.

   7. Javobni Qaytarish
      Shablon render qilinib, tayyor bo'lgach, Django HTTP javobni hosil qiladi va bu javob middleware orqali qaytib, foydalanuvchiga yuboriladi.




**6-task**
  Analytical Questions:
* Find the most borrowed book in the last 6 months.
     SELECT B.title, COUNT(BR.record_id) AS borrow_count
     FROM BorrowingRecords BR
     JOIN Books B ON BR.book_id = B.book_id
     WHERE BR.borrow_date >= CURRENT_DATE - INTERVAL '6 months'
     GROUP BY B.title ORDER BY borrow_count DESC LIMIT 1;
* 
            title            | borrow_count
     -----------------------------+--------------
     Watch somebody at specific. |            6
     (1 row)


* Find the average borrowing duration for books. 
     SELECT M.name, COUNT(BR.record_id) AS borrow_count
     FROM BorrowingRecords BR
     JOIN Members M ON BR.member_id = M.member_id
     GROUP BY M.name ORDER BY borrow_count DESC LIMIT 1;
* 
        name     | borrow_count
     -------------+--------------
     Laura Davis |           27
     (1 row)


* Find the average borrowing duration for books
     SELECT AVG(return_date - borrow_date) AS average_borrowing_duration
     FROM BorrowingRecords
     WHERE return_date IS NOT NULL;
* 
      average_borrowing_duration
     ----------------------------
     370.7094430992736077
    (1 row)