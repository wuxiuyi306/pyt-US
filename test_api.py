import requests
import json

def test_eastmoney_api():
    # 测试获取美股列表的API
    url = "http://72.push2.eastmoney.com/api/qt/clist/get"
    
    # 请求参数
    params = {
        'pn': '1',  # 页码
        'pz': '20',  # 每页数量
        'po': '1',  # 排序方向，1：正序，0：倒序
        'np': '1',  # 是否分页
        'fltt': '2',  # 数据格式
        'invt': '2',  # 排序规则
        'fid': 'f3',  # 排序字段
        'fs': 'm:105,m:106,m:107',  # 市场代码，美股市场
        'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152',
    }
    
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'http://quote.eastmoney.com/',
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        print("状态码:", response.status_code)
        print("\n响应头:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        
        if response.status_code == 200:
            data = response.json()
            print("\n数据示例:")
            print(json.dumps(data, indent=2, ensure_ascii=False)[:1000])  # 只打印前1000个字符
            return True
        else:
            print("请求失败")
            return False
            
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return False

if __name__ == "__main__":
    print("开始测试东方财富网API...")
    success = test_eastmoney_api()
    if success:
        print("\n测试成功：API可以正常访问，不需要特殊认证")
    else:
        print("\n测试失败：可能需要特殊认证或API密钥")
