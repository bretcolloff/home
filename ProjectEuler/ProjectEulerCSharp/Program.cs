using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEulerCSharp
{
    class Program
    {
        public static IEnumerable<int> SieveOfEratosthenes(int limit)
        {
            var filteredFlags = new Dictionary<int, bool>();
            Enumerable.Range(1, limit).ToList().ForEach(x => filteredFlags.Add(x, false));

            for (int i = 2; i <= limit; i++)
            {
                if (filteredFlags[i] == true)
                {
                    continue;
                }

                for (int j = i + i; j <= limit; j += i)
                {
                    filteredFlags[j] = true;
                }
            }

            return filteredFlags.Where(x => x.Value == false).Select(x => x.Key);
        }

        static void Problem50()
        {
            var primes = SieveOfEratosthenes(1000000).ToArray();
            var listOfSums = new List<int>(primes.Count() + 1);
            int total = 0;
            int answer = 0;

            foreach (var prime in primes)
            {
                total += prime;
                listOfSums.Add(total);

                if (total >= 1000000)
                {
                    break;
                }
            }

            int num = 0;
            for (int i = num; i < listOfSums.Count(); i++)
            {
                for (int j = i - (num + 1); j >= 0; j--)
                {
                    if (Array.BinarySearch(primes, listOfSums[i] - listOfSums[j]) >= 0)
                    {
                        num = i - j;
                        answer = listOfSums[i] - listOfSums[j];
                    }
                }
            }
        }

        static void Main(string[] args)
        {
            Problem50();
        }
    }
}
