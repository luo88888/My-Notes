        #include<iostream>
        #include<opencv2/opencv.hpp>
        #include<string>

        using namespace std;
        using namespace cv;

        int main(int argc, char** argv)
        {
            system("color F0");
            //string fileName = "datas.yaml";
            string fileName = "datas.xml";

            FileStorage fwrite(fileName, FileStorage::WRITE);	//以写入的方式打开文件

            //存入矩阵Mat类型的数据
            Mat mat = Mat::eye(3, 3, CV_8U);
            fwrite.write("mat", mat);
            //存入浮点数类型，节点名称为x
            float x = 102;
            fwrite << "x" << x;
            //存入字符串型数据，节点名称为str
            string str = "Learn XML";
            fwrite << "str" << str;
            //存入数组，节点名称为number_array
            fwrite << "number_array" << "[" << 4 << 5 << 6 << "]";
            //存入多node节点数据，主名称为multi_nodes
            fwrite << "multi_nodes" << "{" << "month" << 6 << "day" << 3 << "year" << 2024
                << "time" << "[" << 1 << 6 << 2 << 1 << "]" << "}";
            //关闭文件
            fwrite.release();


            //以读取的模式打开文件
            FileStorage rread(fileName, FileStorage::READ);
            //判断是否成功打开文件
            if (!rread.isOpened())
            {
                cerr << "无法打开文件：" << fileName << endl;
                return -1;
            }

            //读取文件中的数据
            //读取浮点数
            float xRead;
            rread["x"] >> xRead;
            cout << "x=" << xRead << endl;

            //读取字符串
            string strRead;
            rread["str"] >> strRead;
            cout << "str=" << strRead << endl;

            //读取含多个数据的number_array节点
            FileNode fileNode = rread["number_array"];
            cout << "number_array=[";
            //循环遍历每个数据
            for (FileNodeIterator i = fileNode.begin(); i != fileNode.end(); i++)
            {
                float a;
                *i >> a;
                cout << a << " ";
            }
            cout << "]" << endl;

            //读取Mat类数据
            Mat matRead;
            rread["mat"] >> matRead;
            cout << "mat=" << matRead;
            cout << endl;

            //读取含有多个子节点的节点数据，不使用FileNode和迭代器进行读取
            FileNode fileNode1 = rread["multi_nodes"];
            int month = (int)fileNode1["month"];
            int day = (int)fileNode1["day"];
            int year = (int)fileNode1["year"];
            cout << "multi_nodes:" << endl
                << " month=" << month << " day=" << day << " year=" << year<< " time=[";
            for (int i = 0; i < 4; i++)
            {
                int a = (int)fileNode1["time"][i];
                cout << a << " ";
            }
            cout << "]" << endl;

            //关闭文件
            rread.release();
            return 0;
        }