-- 支持事务的存储过程
delimiter \\
create PROCEDURE p1(
    OUT p_return_code tinyint    -- 设置形参
)
BEGIN
  DECLARE exit handler for sqlexception  -- 捕获错误异常
  BEGIN
    -- ERROR
    set p_return_code = 1;
    rollback;
  END;

  DECLARE exit handler for sqlwarning
  BEGIN
    -- WARNING
    set p_return_code = 2;
    rollback;
  END;

  START TRANSACTION;
    DELETE from tb1;
    insert into tb2(name)values('seven');
  COMMIT;

  -- SUCCESS
  set p_return_code = 0;

  END\\
delimiter ;

--游标
delimiter //
create procedure p3()
begin
    declare ssid int; -- 自定义变量1
    declare ssname varchar(50); -- 自定义变量2
     -- 遍历数据结束标志
    DECLARE done INT DEFAULT FALSE;


    DECLARE my_cursor CURSOR FOR select sid,sname from student;  -- 声明游标
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;  -- -- 将结束标志绑定到游标

    open my_cursor; -- 打开游标
        xxoo: LOOP
        -- 逐个取出当前记录的字段的值,
            fetch my_cursor into ssid,ssname;
            if done then
                leave xxoo;  -- done 是 true的话跳过  即找不到的时候跳出
            END IF;
            insert into teacher(tname) values(ssname); --找到了插入一条数据
        end loop xxoo;
    close my_cursor;  -- 关闭游标
end  //
delimter ;
-- 只有发现一条的时候才插入teacher表


-- 动态执行sql---存储过程
delimiter \\
CREATE PROCEDURE p10 (
in nid int
)
BEGIN
set @id = nid; -- 必须找个格式
PREPARE prod FROM 'select * from student where sid > ?';
EXECUTE prod USING @id;
DEALLOCATE prepare prod;
END\\
delimiter ;

@id = 10;
call p4(1);


drop procedure p10; -- 删除存储过程


show create procedure p4;  -- 查看存储过程
