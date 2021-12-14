Delimiter $$
CREATE trigger reserved_update after update on locker_users
for each row
begin
	UPDATE locker_lockers set locker_lockers.reserved=1 where locker_lockers.lockernum=NEW.lockernum;
    UPDATE locker_lockers set locker_lockers.reserved=0 where locker_lockers.lockernum=OLD.lockernum;
end$$
Delimiter ;