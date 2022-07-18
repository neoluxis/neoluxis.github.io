# 科学上网安卓客户端——AnXray

## 前言

目前最流行使用[Xray](https://github.com/XTLS/Xray-core/releases/tag/v1.4.2)科学翻墙技术应 用 于 服 务 端 ， 在 Window 电 脑 使 用 [Winxray 客 户 端 ](https://github.com/hans822418/winXray-3.7)连 接 ， Macos 使 用 [Qxray](https://github.com/Qv2ray/Qv2ray/releases/download/v2.7.0/Qv2ray-v2.7.0-macOS-x64.dmg)客户端,那么Andorid手机则使用**AnXray**客户端。 对！今天重点介绍的就是**AnXray**客户端，一起先来看看长什么样吧！

![image](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-16578084848041.png)


## 下载
看完界面是不是很酷！**AnXray**发行有许多版本，兼容性非常好。对不清楚下载哪个版本的朋友可以 先看个究竟再决定，如下图目前发布最新的0.1-beta06版本.

arm64 v8a适合性能佳的安卓手机下载(像高通骁龙(snapdragon),三星(Exynos),联发科(Helio).华为(麒 麟))，arm64 v8a[下载链接](https://github.com/XTLS/AnXray/releases/download/0.1-beta06/AX-0.1-beta06-arm64-v8a.apk)。 arm64 v7a是刚过失的前主流手机下载，对于老牙手机兼容好， 大多数请使用arm64 v8a版本安装 ，如果 安装失败再考虑arm64 v7a,[下载链接 ](https://github.com/XTLS/AnXray/releases/download/0.1-beta06/AX-0.1-beta06-armeabi-v7a.apk)。 大家根据自己的手机情况下载。 查 看 更 全 面 各 版 本 的 apk 安 装 包 详 见[此处](https://github.com/XTLS/AnXray/releases/tag/0.1- beta06)

![image-1657511289558](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-1657511289558-16578085078343.png)

## 支持协议类型
如果说V2rayNG是之前地表最好用的主流安卓客户端，那么AnXray也不例外，形象比喻地表有了 它们两个，V2rayNG从此告别脱单！ 一起看看AnXray到底有多强大，看看支持的协议就明白了。

1. SOCKS 
2. HTTP(S)
3. Shadowsocks
4. ShadowsocksR
5. VMess
6. VLess with XTLS support
7. Trojan with XTLS support
8. Trojan-Go ( trojan-go-plugin )
9. NaïveProxy ( naive-plugin )
10. Ping Tunnel ( pingtunnel-plugin )
11. relaybaton ( relaybaton-plugin )
12. Brook ( brook-plugin )

上述12种协议已打包到程序中，不像一些程序(如：Qv2ray)需要安装相应插件才可使用。这就是 AnXray 的 最 大 优 势 所 在 。 它 比 V2rayNG 多 了 Trojan-go,NaivePorxy,Ping Tunnel,relaybaton,Brook协议。真的鸟不得！ 只要安装上它， *一机在手，走遍天下我都有。*

## 支持订阅类型
* Universial base64
	```powershell
	c3NyOi8vZW5ndWFHc3VNREV1TURJdWVHWnFMVzV2WkdVdWRHOXdPakl6TXpNNllYVjBhRjloWlhNeE1qaGZiV1ExT25Kak5DMXRaRFU2YUhSMGNGOXphVzF3YkdVNlVtMDFiazVZVlRSU1NHc3ZQMjlpWm5Od1lYSmhiVDFaZWxac1QwUnJlVTVVUVhoT2FUVnhXa00xYjJGM0puQnliM1J2Y0dGeVlXMDlUV3BWZDAxVVdUWlBSazB6WTFSQ2J5WnlaVzFoY210elBWRXdOSFJTTUZGME5XSnRYelZNYVdOTVZFVTBUWGt4YUdKSGJEVmtWelIxV1RJNWRDWm5jbTkxY0QxaVdGWjBXVlJGTWxwdVp3CnNzcjovL2RIY3lMbTk1ZG5CdWMyVnlkbVZ5TG1OdmJUb3pOVGN5T205eWFXZHBianB5WXpRdGJXUTFPbkJzWVdsdU9sa3lhREJOVkdzMVRuazBkVXhwT0haTWR5OF9iMkptYzNCaGNtRnRQU1p5WlcxaGNtdHpQVkV3TkhSV1JtTjBOVmt0ZHpWeWJTMU1WRTB4VEZkT2IyUkROV3BpTWpCMVpFaGpKbWR5YjNWd1BXSllWblJaVkVVeVdtNW4Kc3NyOi8vTWpFeExqYzFMamM1TGpJek16b3hOalV3TlRwdmNtbG5hVzQ2WVdWekxUSTFOaTFqWm1JNmNHeGhhVzQ2VlZjNU5tVnVWalpVU0UxNVZucE5lUzhfYjJKbWMzQmhjbUZ0UFNaeVpXMWhjbXR6UFZFd05IUldSbU4wTlZrdGR6VnliUzFNVkVsNlRYa3hhbUZJVVhWWk1qbDBURzVTTXlabmNtOTFjRDFpV0ZaMFdWUkZNbHB1WncKc3NyOi8vYzJkd01pNXZlWFp3Ym5ObGNuWmxjaTVqYjIwNk16VTNNanB2Y21sbmFXNDZjbU0wTFcxa05UcHdiR0ZwYmpwWk1tZ3dUVlJyTlU1NU5IVk1hVGgyVEhjdlAyOWlabk53WVhKaGJUMG1jbVZ0WVhKcmN6MVRiRUYwTlhCbGJEVndlWE5NWlZNMGJrOVRObkpETUhoT1ZFRjBUV2t4TUdGSGJIVmhNbWd4V2pKVmRXSnRWakFtWjNKdmRYQTlZbGhXZEZsVVJUSmFibWMKc3NyOi8vYW5BekxtOTVkbkJ1YzJWeWRtVnlMbU52YlRvek5UY3lPbTl5YVdkcGJqcHlZelF0YldRMU9uQnNZV2x1T2xreWFEQk5WR3MxVG5rMGRVeHBPSFpNZHk4X2IySm1jM0JoY21GdFBTWnlaVzFoY210elBWTnNRWFExY0dWc05YQjVjMHhsVXpSdVQxTTJja013ZUU1VVFYUk5lVEV3WVVkc2RXRXlhREZhTWxWMVltMVdNQ1puY205MWNEMWlXRlowV1ZSRk1scHVadwpzc3I6Ly9ORFV1TmpjdU5UTXVNalV3T2pRME16cHZjbWxuYVc0NllXVnpMVEkxTmkxalptSTZjR3hoYVc0NlpETmtNMHh1YUdsa2JrSjFURzFPZG1KUkx6OXZZbVp6Y0dGeVlXMDlKbkpsYldGeWEzTTlVMnhCZERWd1pXdzFjSGx6VEdWVE5HNVBVelp5UXpCNVRsUkJkR1JIYUhCaWJYUnZaRmRrYkV4dE5XeGtRU1puY205MWNEMWlXRlowV1ZSRk1scHVadwpzc3I6Ly9ORFV1TnprdU5qWXVPVG8wTkRNNmIzSnBaMmx1T21GbGN5MHlOVFl0WTJaaU9uQnNZV2x1T2s5WFVUSlpNazVzV1ZkRmVrNTZUbWxhYWtwcVQwZEdhbGxxU1hsYVZGbDNXV3BhYUU1VWFHbGFWRmt2UDI5aVpuTndZWEpoYlQwbWNtVnRZWEpyY3oxV1ZrNUNUR1ZsTFdwMVYySjJVek52ZEV4dWJHbExibTlyY0d0MFQxTXhjMkZYTlhaYVIxVjFXVEk1ZENabmNtOTFjRDFpV0ZaMFdWUkZNbHB1WncKc3NyOi8vTkRVdU56a3VNVEE0TGpFeU9qUTBNenB2Y21sbmFXNDZZV1Z6TFRJMU5pMWpabUk2Y0d4aGFXNDZUMWRSTWxreVRteFpWMFY2VG5wT2FWcHFTbXBQUjBacVdXcEplVnBVV1hkWmFscG9UbFJvYVZwVVdTOF9iMkptYzNCaGNtRnRQU1p5WlcxaGNtdHpQVlpXVGtKTVpXVXRhblZYWW5aVE0yOTBURzVzYVV0dWIydHdhM1JOVkVsMFlrZHNkV0l5VW14TWJVNTJZbEVtWjNKdmRYQTlZbGhXZEZsVVJUSmFibWMKc3NyOi8vTkRVdU56a3VOemt1TXpjNk5EUXpPbTl5YVdkcGJqcGhaWE10TWpVMkxXTm1ZanB3YkdGcGJqcFBWMUV5V1RKT2JGbFhSWHBPZWs1cFdtcEthazlIUm1wWmFrbDVXbFJaZDFscVdtaE9WR2hwV2xSWkx6OXZZbVp6Y0dGeVlXMDlKbkpsYldGeWEzTTlWbFpPUWt4bFpTMXFkVmRpZGxNemIzUk1ibXhwUzI1dmEzQnJkRTE2WTNSaVIyeDFZakpTYkV4dFRuWmlVU1puY205MWNEMWlXRlowV1ZSRk1scHVadwpzc3I6Ly9ORFV1TlRZdU9UUXVOREE2TkRRek9tOXlhV2RwYmpwaFpYTXRNalUyTFdObVlqcHdiR0ZwYmpwUFYxRXlXVEpPYkZsWFJYcE9lazVwV21wS2FrOUhSbXBaYWtsNVdsUlpkMWxxV21oT1ZHaHBXbFJaTHo5dlltWnpjR0Z5WVcwOUpuSmxiV0Z5YTNNOVZsWk9Ra3hsWlMxcWRWZGlkbE16YjNSTWJteHBTMjV2YTNCcmRFNUVRWFJPUkZGNlRGZDRjR0p0T1d0YVV6VnFZakl3Sm1keWIzVndQV0pZVm5SWlZFVXlXbTVuCnNzcjovL05UQXVNVEUyTGpJdU1UTXhPalEwTXpwdmNtbG5hVzQ2WVdWekxUSTFOaTFqWm1JNmNHeGhhVzQ2VDFkUk1sa3lUbXhaVjBWNlRucE9hVnBxU21wUFIwWnFXV3BKZVZwVVdYZFphbHBvVGxSb2FWcFVXUzhfYjJKbWMzQmhjbUZ0UFNaeVpXMWhjbXR6UFZaV1RrSk1aV1V0YW5WWFluWlRNMjkwVEc1c2FVdHViMnR3YTNSTlZFMHdURlJSTUUxNU1YTmhWelYyV2tkVmRWa3lPWFFtWjNKdmRYQTlZbGhXZEZsVVJUSmFibWMKc3NyOi8vTkRVdU56a3VPVE11TVRjNE9qUTBNenB2Y21sbmFXNDZZV1Z6TFRJMU5pMWpabUk2Y0d4aGFXNDZUMWRSTWxreVRteFpWMFY2VG5wT2FWcHFTbXBQUjBacVdXcEplVnBVV1hkWmFscG9UbFJvYVZwVVdTOF9iMkptYzNCaGNtRnRQU1p5WlcxaGNtdHpQVlpXVGtKTVpXVXRhblZYWW5aVE0yOTBURzVzYVV0dWIydHdhM1JOVkdNMFRGZDRjR0p0T1d0YVV6VnFZakl3Sm1keWIzVndQV0pZVm5SWlZFVXlXbTVuCnNzcjovL05EVXVNekl1T1RNdU1UUTNPakUyTmpBNE9tRjFkR2hmWTJoaGFXNWZZVHBoWlhNdE1qVTJMV05tWWpwb2RIUndYM05wYlhCc1pUcFJWMFY1VFVSRk1VMUVaM2ROVTI4dlAyOWlabk53WVhKaGJUMG1jbVZ0WVhKcmN6MVdWazVDVEdWbExXcDFWMkoyVXpOdGRFcDJiVzVaYm01dU4xbDBUVlJSTTB4WFRtOWlNamwzV1ZNMWFtSXlNQ1puY205MWNEMWlXRlowV1ZSRk1scHVadwpzc3I6Ly9kWE5oTVM1dmVYWndibk5sY25abGNpNWpiMjA2TXpVM01qcHZjbWxuYVc0NmNtTTBMVzFrTlRwd2JHRnBianBaTW1nd1RWUnJOVTU1TkhWTWFUaDJUSGN2UDI5aVpuTndZWEpoYlQwbWNtVnRZWEpyY3oxV1ZrNUNUR1ZsTFdwMVYySjJVek50ZEVwMmJXNVpibTV1TjFsMFRWUlpkMHhVUlhSWk1qbHpZakpPZVdJelRucGhWelZ1VEcxT2RtSlJKbWR5YjNWd1BXSllWblJaVkVVeVdtNW4Kc3NyOi8vZFhOaE1pNXZlWFp3Ym5ObGNuWmxjaTVqYjIwNk16VTNNanB2Y21sbmFXNDZjbU0wTFcxa05UcHdiR0ZwYmpwWk1tZ3dUVlJyTlU1NU5IVk1hVGgyVEhjdlAyOWlabk53WVhKaGJUMG1jbVZ0WVhKcmN6MVdWazVDVEdWbExXcDFWMkoyVXpOdGRFcDJiVzVaYm01dU4xbDBUVlJaZDB4VVNYUlpNamx6WWpKT2VXSXpUbnBoVnpWdVRHMU9kbUpSSm1keWIzVndQV0pZVm5SWlZFVXlXbTVuCnNzcjovL2RYTmhOUzV2ZVhad2JuTmxjblpsY2k1amIyMDZNelUzTWpwdmNtbG5hVzQ2Y21NMExXMWtOVHB3YkdGcGJqcFpNbWd3VFZSck5VNTVOSFZNYVRoMlRIY3ZQMjlpWm5Od1lYSmhiVDBtY21WdFlYSnJjejFXVms1Q1RHVmxMV3AxVjJKMlV6TnRkRXAyYlc1WmJtNXVOMWwwVFZSWmQweFVWWFJaTWpsellqSk9lV0l6VG5waFZ6VnVURzFPZG1KUkptZHliM1Z3UFdKWVZuUlpWRVV5V201bgpzc3I6Ly9ORFV1TXpNdU9EZ3VNVGt3T2pRME16cHZjbWxuYVc0NllXVnpMVEkxTmkxalptSTZjR3hoYVc0NlQxZFJNbGt5VG14WlYwVjZUbnBPYVZwcVNtcFBSMFpxV1dwSmVWcFVXWGRaYWxwb1RsUm9hVnBVV1M4X2IySm1jM0JoY21GdFBTWnlaVzFoY210elBWWldUa0pNWldVdGFuVlhZblpUTTI1MWNqTnVhelppYkdoWmMzUk5lVEZ6WVZjMWRscEhWWFZaTWpsMEptZHliM1Z3UFdKWVZuUlpWRVV5V201bgpzc3I6Ly9ORFV1TXpNdU9UTXVNakEzT2pRME16cHZjbWxuYVc0NllXVnpMVEkxTmkxalptSTZjR3hoYVc0NlQxZFJNbGt5VG14WlYwVjZUbnBPYVZwcVNtcFBSMFpxV1dwSmVWcFVXWGRaYWxwb1RsUm9hVnBVV1M4X2IySm1jM0JoY21GdFBTWnlaVzFoY210elBWWldUa0pNWldVdGFuVlhZblpUTTI1MWNqTnVhelppYkdoWmMzUk9RekZ6WVZjMWRscEhWWFZaTWpsMEptZHliM1Z3UFdKWVZuUlpWRVV5V201bgpzc3I6Ly9NakEzTGpFME9DNHhPUzR4TVRNNk1UWXlNRGs2WVhWMGFGOWphR0ZwYmw5aE9tRmxjeTB5TlRZdFkyWmlPbWgwZEhCZmMybHRjR3hsT2xGWFJYbE5SRVV4VFVSbmQwMVRieThfYjJKbWMzQmhjbUZ0UFNaeVpXMWhjbXR6UFZaV1RrSk1aV1V0YW5WWFluWlRNMjV0Y1RkdGJIRmZiR3BoU0c1cFltNXVkVGRSZEUxVVJYcE1WMDV2WWpJNWQxbFROV3BpTWpBbVozSnZkWEE5WWxoV2RGbFVSVEphYm1jCnNzcjovL05EVXVOVGd1TVRRNExqWTJPakl4TnpZek9tOXlhV2RwYmpwaFpYTXRNalUyTFdObVlqcHdiR0ZwYmpwT1JtaFhXbFpCZUM4X2IySm1jM0JoY21GdFBTWnlaVzFoY210elBWUnJlRVZNWldsT2RDMVhSbk5ETTNCdFRGOXNjRFJpYld4eFgyNXBZbTVyZFV4cmRFNXFXWFJqTW1ob1kyMTBNRnBYVG05TWJUVnNaRUVtWjNKdmRYQTlZbGhXZEZsVVJUSmFibWMK
	```
	
	
	比如这样的Base64编码的信息，可以<kbd>全选+复制</kbd>然后在手机端利用AnXray的“从剪切板导入”，完成节点的导入
	
* Shadowsocks SIP008

    导入方法如上，不再赘述。

* Just My Socks’ proprietary format

    暂时没有Just My Socks的产品，所以没有展示

* Clash

    ```powershell
    port: 7890
    socks-port: 7891
    allow-lan: true
    mode: Rule
    log-level: info
    external-controller: 127.0.0.1:9090
    proxies:
      - {name: 🇺🇲 adi|0529 - 美国, server: 104.200.131.245, port: 44820, type: ss, cipher: aes-256-gcm, password: jspgz9G3VmvBMCgMUWLBaZHu}
      - {name: adi|0519 - 2, server: 104.200.131.245, port: 49396, type: ss, cipher: aes-256-gcm, password: BdRWC38L5JUDMTYNNxJGcUwB}
      - {name: 🇺🇲 adi|0528 - 美国, server: 104.200.131.245, port: 49339, type: ss, cipher: aes-256-gcm, password: suucSeVLmt6PQKAP77NtGw9x}
      - {name: adi|0523 - 167.88.63.29:806, server: 167.88.63.29, port: 806, type: ss, cipher: chacha20-ietf-poly1305, password: G!yBwPWH3Vao}
      - {name: 🇺🇲 adi|0528 - 美国 2, server: 104.200.131.245, port: 49126, type: ss, cipher: aes-256-gcm, password: wrCaGtrUbzeRqQLdc8Kmk3Nd}
      - {name: 🇺🇲 adi|0529 - 美国ss15, server: ss.us.sshmax.net, port: 57478, type: ss, cipher: chacha20-ietf-poly1305, password: syCiJl3nb8OD}
      - {name: 🇺🇲 adi|0529 - 美国 2, server: 104.200.131.245, port: 33148, type: ss, cipher: aes-256-gcm, password: CMduaFXddcQbwNAAs7xFDnc8}
      - {name: 🇺🇲 adi|0529 - 美国 3, server: 104.200.131.245, port: 40093, type: ss, cipher: aes-256-gcm, password: x23Z4LGkGDkThZ9Kaz4DURQp}
      - {name: 🇺🇲 adi|0527 - 美国, server: 207.244.67.149, port: 40093, type: ss, cipher: aes-256-gcm, password: x23Z4LGkGDkThZ9Kaz4DURQp}
      - {name: adi|0527 - 🇺🇸, server: 104.200.131.165, port: 33992, type: ss, cipher: aes-256-gcm, password: 8n6pwAcrrv2pj6tFY2p3TbQ6}
      - {name: adi|0523 - 135.125.248.215:811, server: 135.125.248.215, port: 811, type: ss, cipher: chacha20-ietf-poly1305, password: G!yBwPWH3Vao}
      - {name: 🇿🇦 adi|0507 - 南非, server: 154.127.50.138, port: 31572, type: ss, cipher: aes-256-gcm, password: n8w4StnbVD9dmXYn4Ajt87EA}
      - {name: adi|0527 - 003013151, server: 139.28.176.53, port: 31572, type: ss, cipher: aes-256-gcm, password: n8w4StnbVD9dmXYn4Ajt87EA}
      - {name: 🇷🇴 adi|0527 - Pool_🇷🇴RO_2446, server: 91.90.121.163, port: 31572, type: ss, cipher: aes-256-gcm, password: n8w4StnbVD9dmXYn4Ajt87EA}
      - {name: adi|0519 - 9, server: 154.127.50.138, port: 31944, type: ss, cipher: aes-256-gcm, password: aYNeKDMzYQYw4KbUbJA8Wszq}
      - {name: 🇺🇲 adi|0529 - 美国CFCDN 6, server: 104.18.6.138, port: 443, type: vmess, uuid: 3b5e258e-8c5e-45d3-b7d2-02c8f5fc0bb2, alterId: 64, cipher: auto, tls: true, network: ws, ws-path: /, ws-headers: {Host: cdnde.irteyz.today}}
      - {name: 🇺🇲 adi|0529 - 美国CFCDN 7, server: 104.21.48.161, port: 443, type: vmess, uuid: 3b5e258e-8c5e-45d3-b7d2-02c8f5fc0bb2, alterId: 64, cipher: auto, tls: true, network: ws, ws-path: /, ws-headers: {Host: cdnde.irteyz.today}}
      - {name: adi|0527 - |18.04Mb, server: 104.225.239.212, port: 443, type: vmess, uuid: 3621eb66-1049-4e86-b0e3-d1643ccacd7c, alterId: 60, cipher: auto, tls: true, network: ws, ws-path: /asdfasdf, ws-headers: {Host: 104.225.239.212}}
      - {name: 🇺🇲 adi|0529 - 美国CF 8, server: cdnde.irteyz.today, port: 443, type: vmess, uuid: 3b5e258e-8c5e-45d3-b7d2-02c8f5fc0bb2, alterId: 64, cipher: auto, tls: true, network: ws, ws-path: /, ws-headers: {Host: cdnde.irteyz.today}}
      - {name: 🇺🇲 adi|0529 - 美国CFCDN 10, server: 104.18.7.138, port: 443, type: vmess, uuid: 3b5e258e-8c5e-45d3-b7d2-02c8f5fc0bb2, alterId: 64, cipher: auto, tls: true, network: ws, ws-path: /, ws-headers: {Host: cdnde.irteyz.today}}
      - {name: adi|0528 - | 3.87Mb, server: bimbel.ruangguru.com, port: 80, type: vmess, uuid: b22b990f-b6dd-4b57-a0e1-ee3f829d413f, alterId: 64, cipher: auto, tls: false, network: ws, ws-path: /sshkit, ws-headers: {Host: eu-sshkit.v2-ray.cf}}
      - {name: 🇺🇲 adi|0529 - 美国CF 8 2, server: 172.67.154.85, port: 443, type: vmess, uuid: 3b5e258e-8c5e-45d3-b7d2-02c8f5fc0bb2, alterId: 64, cipher: auto, tls: true, network: ws, ws-path: /, ws-headers: {Host: cdnde.irteyz.today}}
    proxy-groups:
      - name: 🚀 节点选择
        type: select
        proxies:
          - ♻️ 自动选择
          - DIRECT
          - 🇺🇲 adi|0529 - 美国
          - adi|0519 - 2
          - 🇺🇲 adi|0528 - 美国
          - adi|0523 - 167.88.63.29:806
          - 🇺🇲 adi|0528 - 美国 2
          - 🇺🇲 adi|0529 - 美国ss15
          - 🇺🇲 adi|0529 - 美国 2
          - 🇺🇲 adi|0529 - 美国 3
          - 🇺🇲 adi|0527 - 美国
          - adi|0527 - 🇺🇸
          - adi|0523 - 135.125.248.215:811
          - 🇿🇦 adi|0507 - 南非
          - adi|0527 - 003013151
          - 🇷🇴 adi|0527 - Pool_🇷🇴RO_2446
          - adi|0519 - 9
          - 🇺🇲 adi|0529 - 美国CFCDN 6
          - 🇺🇲 adi|0529 - 美国CFCDN 7
          - adi|0527 - |18.04Mb
          - 🇺🇲 adi|0529 - 美国CF 8
          - 🇺🇲 adi|0529 - 美国CFCDN 10
          - adi|0528 - | 3.87Mb
          - 🇺🇲 adi|0529 - 美国CF 8 2
      - name: ♻️ 自动选择
        type: url-test
        url: http://www.gstatic.com/generate_204
        interval: 300
        tolerance: 50
        proxies:
          - 🇺🇲 adi|0529 - 美国
          - adi|0519 - 2
          - 🇺🇲 adi|0528 - 美国
          - adi|0523 - 167.88.63.29:806
          - 🇺🇲 adi|0528 - 美国 2
          - 🇺🇲 adi|0529 - 美国ss15
          - 🇺🇲 adi|0529 - 美国 2
          - 🇺🇲 adi|0529 - 美国 3
          - 🇺🇲 adi|0527 - 美国
          - adi|0527 - 🇺🇸
          - adi|0523 - 135.125.248.215:811
          - 🇿🇦 adi|0507 - 南非
          - adi|0527 - 003013151
          - 🇷🇴 adi|0527 - Pool_🇷🇴RO_2446
          - adi|0519 - 9
          - 🇺🇲 adi|0529 - 美国CFCDN 6
          - 🇺🇲 adi|0529 - 美国CFCDN 7
          - adi|0527 - |18.04Mb
          - 🇺🇲 adi|0529 - 美国CF 8
          - 🇺🇲 adi|0529 - 美国CFCDN 10
          - adi|0528 - | 3.87Mb
          - 🇺🇲 adi|0529 - 美国CF 8 2
      - name: 🎯 全球直连
        type: select
        proxies:
          - DIRECT
          - 🚀 节点选择
          - ♻️ 自动选择
      - name: 🛑 全球拦截
        type: select
        proxies:
          - REJECT
          - DIRECT
      - name: 🐟 漏网之鱼
        type: select
        proxies:
          - 🚀 节点选择
          - 🎯 全球直连
          - ♻️ 自动选择
          - 🇺🇲 adi|0529 - 美国
          - adi|0519 - 2
          - 🇺🇲 adi|0528 - 美国
          - adi|0523 - 167.88.63.29:806
          - 🇺🇲 adi|0528 - 美国 2
          - 🇺🇲 adi|0529 - 美国ss15
          - 🇺🇲 adi|0529 - 美国 2
          - 🇺🇲 adi|0529 - 美国 3
          - 🇺🇲 adi|0527 - 美国
          - adi|0527 - 🇺🇸
          - adi|0523 - 135.125.248.215:811
          - 🇿🇦 adi|0507 - 南非
          - adi|0527 - 003013151
          - 🇷🇴 adi|0527 - Pool_🇷🇴RO_2446
          - adi|0519 - 9
          - 🇺🇲 adi|0529 - 美国CFCDN 6
          - 🇺🇲 adi|0529 - 美国CFCDN 7
          - adi|0527 - |18.04Mb
          - 🇺🇲 adi|0529 - 美国CF 8
          - 🇺🇲 adi|0529 - 美国CFCDN 10
          - adi|0528 - | 3.87Mb
          - 🇺🇲 adi|0529 - 美国CF 8 2
    rules:
     - DOMAIN-SUFFIX,acl4.ssr,🎯 全球直连
     - DOMAIN-SUFFIX,ip6-localhost,🎯 全球直连
     - DOMAIN,livew.l.qq.com,🎯 全球直连
     - DOMAIN,vd.l.qq.com,🎯 全球直连
     - DOMAIN,analytics.strava.com,🎯 全球直连
     - DOMAIN,msg.umeng.com,🎯 全球直连
     - DOMAIN,msg.umengcloud.com,🎯 全球直连
     - DOMAIN,tracking.miui.com,🎯 全球直连
     - DOMAIN,app.adjust.com,🎯 全球直连
     - DOMAIN,bdtj.tagtic.cn,🎯 全球直连
     - DOMAIN-KEYWORD,admarvel,🛑 全球拦截
     - DOMAIN-KEYWORD,admaster,🛑 全球拦截
     - DOMAIN-SUFFIX,swq48b.cn,🛑 全球拦截
     - DOMAIN-SUFFIX,265.com,🎯 全球直连
     - DOMAIN-SUFFIX,2mdn.net,🎯 全球直连
     - DOMAIN-SUFFIX,alt1-mtalk.google.com,🎯 全球直连
     - DOMAIN-SUFFIX,alt2-mtalk.google.com,🎯 全球直连
     - DOMAIN-SUFFIX,alt3-mtalk.google.com,🎯 全球直连
     - DOMAIN-SUFFIX,alt4-mtalk.google.com,🎯 全球直连
     - DOMAIN-SUFFIX,alt5-mtalk.google.com,🎯 全球直连
     - DOMAIN-SUFFIX,alt6-mtalk.google.com,🎯 全球直连
     - DOMAIN-SUFFIX,alt7-mtalk.google.com,🎯 全球直连
     - DOMAIN-SUFFIX,alt8-mtalk.google.com,🎯 全球直连
     - DOMAIN-SUFFIX,app-measurement.com,🎯 全球直连
     - DOMAIN-SUFFIX,c.android.clients.google.com,🎯 全球直连
     - DOMAIN-SUFFIX,cache.pack.google.com,🎯 全球直连
     - DOMAIN-SUFFIX,clickserve.dartsearch.net,🎯 全球直连
     - DOMAIN-SUFFIX,clientservices.googleapis.com,🎯 全球直连
     - DOMAIN-SUFFIX,t.me,🚀 节点选择
     - DOMAIN-SUFFIX,tdesktop.com,🚀 节点选择
     - DOMAIN-SUFFIX,telegra.ph,🚀 节点选择
     - DOMAIN-SUFFIX,telegram.me,🚀 节点选择
     - DOMAIN-SUFFIX,telegram.org,🚀 节点选择
     - DOMAIN-SUFFIX,telesco.pe,🚀 节点选择
     - IP-CIDR,91.108.0.0/16,🚀 节点选择,no-resolv
     - DOMAIN-SUFFIX,ocnttv.com,🚀 节点选择
     - DOMAIN-SUFFIX,423down.com,🎯 全球直连
     - DOMAIN-SUFFIX,bokecc.com,🎯 全球直连
     - DOMAIN-SUFFIX,chaipip.com,🎯 全球直连
     - DOMAIN-SUFFIX,chinaplay.store,🎯 全球直连
     - DOMAIN-SUFFIX,hrtsea.com,🎯 全球直连
     - DOMAIN-SUFFIX,kaikeba.com,🎯 全球直连
     - DOMAIN-SUFFIX,laomo.me,🎯 全球直连
     - DOMAIN-SUFFIX,mpyit.com,🎯 全球直连
     - GEOIP,CN,🎯 全球直连
     - MATCH,🐟 漏网之鱼
    ```

    以上是一个简版的Clash yaml文件信息，只要将上述代码<kbd>Ctrl</kbd>+<kbd>A</kbd>,<kbd>Ctrl</kbd>+<kbd>C</kbd>，即可在AnXray导入。这 在手机端科学翻墙软件中导入，我首次见到的“强大性”。

    因该Clash yaml文件信息量太大，所以上述代码信息不完整，需要实验的朋友可以直接打开[这个链接](https://raw.githubusercontent.com/adiwzx/freenode/main/adispeed.yml)实验一把。

## 后记
通过以上分享，我没有分享它的各协议的具体使用方法，只是分享它支持的各订阅链接使用方法， 以方便在手机端快捷导入使用。

---------------------------
希望各位朋友喜欢，文中若存在不足或更好的建议，欢迎给我留言。