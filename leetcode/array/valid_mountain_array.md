# Valid Mountain Array 풀이 정리

> LeetCode · Fun with Arrays · Searching for Items in an Array

## 1. 문제 정의

정수 배열 `arr`가 주어졌을 때, 이 배열이 **유효한 산 배열(valid mountain array)**인지 판별하는 문제입니다.

유효한 산 배열의 조건은 다음과 같습니다.

- `arr.length >= 3`
- 어떤 인덱스 `i` (단, `0 < i < arr.length - 1`)가 존재하여 다음을 모두 만족:
  - `arr[0] < arr[1] < ... < arr[i]` (엄격히 증가)
  - `arr[i] > arr[i+1] > ... > arr[arr.length - 1]` (엄격히 감소)

즉, 봉우리(peak)가 **정확히 하나**이며, 그 봉우리는 배열의 **양 끝이 아닌 중간 어딘가**에 위치해야 하고, 양쪽 모두 **strict monotonic**이어야 합니다.

### 엣지 케이스
| 입력 | 결과 | 이유 |
|---|---|---|
| `[2, 1]` | `false` | 길이 부족 |
| `[3, 5, 5]` | `false` | 동일 원소 (strict 위배) |
| `[0, 3, 2, 1]` | `true` | 정상 |
| `[3, 2, 1]` | `false` | 증가 구간이 없음 (peak가 인덱스 0) |
| `[1, 2, 3]` | `false` | 감소 구간이 없음 (peak가 마지막 인덱스) |

---

## 2. 접근 방법

**상태 머신 기반 단일 순회(one-pass)** 방식으로 접근했습니다.

두 개의 불리언 플래그를 사용합니다.

- `increase`: 현재 **증가 구간**을 훑고 있는지 여부 (초기값 `True`)
- `peak_found`: 봉우리를 **한 번이라도 발견했는지** 여부 (초기값 `False`)

배열을 한 번만 순회하면서, 인접한 두 원소 `arr[i]`, `arr[i+1]`을 비교해 다음 네 가지 상황을 처리합니다.

1. **두 원소가 같을 때** → strict 조건 위배이므로 즉시 `False`
2. **증가 중인데 감소가 시작될 때** → 봉우리 발견
   - 단, `i == 0`이면 증가 구간이 전혀 없었다는 뜻이므로 `False`
   - 아니면 `increase = False`, `peak_found = True`로 전환
3. **감소 중인데 다시 증가할 때** → 산 모양이 깨졌으므로 `False`
4. 순회를 모두 마쳤다면, 봉우리가 실제로 나왔는지 (`peak_found`) 반환

이때 `peak_found` 체크가 중요합니다. 그래야 `[1, 2, 3]`처럼 **계속 증가만 하는 배열**도 올바르게 `False`로 걸러낼 수 있습니다.

```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        increase = True
        peak_found = False
        for i in range(len(arr) - 1):
            if arr[i] == arr[i+1]:
                return False
            if increase and arr[i] > arr[i+1]:
                if i == 0:
                    return False
                increase = False
                peak_found = True
            if not increase and arr[i] < arr[i+1]:
                return False
        return peak_found
```

---

## 3. 시간 복잡도 · 공간 복잡도

- **시간 복잡도: O(n)** — 배열을 정확히 한 번 순회합니다.
- **공간 복잡도: O(1)** — 플래그 두 개만 사용하므로 입력 크기와 무관한 상수 공간만 사용합니다.

이 문제는 원리상 모든 원소를 최소 한 번은 확인해야 하므로 `O(n)`이 **이론적 하한**입니다. 즉, 점근적 복잡도 관점에서는 이미 최적입니다.

---

## 4. 개선 사항

### 4-1. 가독성 — Two-pass (두 번의 while 루프)

현재 풀이는 정답이지만, 하나의 루프 안에서 "증가 구간 처리 / 봉우리 전환 / 감소 구간 처리"가 **플래그로 얽혀 있어** 읽기가 다소 복잡합니다.

루프를 두 단계로 나누면 **의도가 코드에 그대로 드러납니다.**

```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0
        # 1) 증가 구간을 최대한 올라간다
        while i + 1 < n and arr[i] < arr[i+1]:
            i += 1
        # 2) 봉우리가 양 끝에 있으면 산이 아니다
        if i == 0 or i == n - 1:
            return False
        # 3) 감소 구간을 끝까지 내려간다
        while i + 1 < n and arr[i] > arr[i+1]:
            i += 1
        # 4) 끝까지 왔다면 유효한 산
        return i == n - 1
```

장점:
- 플래그 변수가 사라져 **상태 관리가 필요 없음**
- "올라간다 → 봉우리 확인 → 내려간다" 흐름이 **자연어 설명과 1:1 대응**
- `arr[i] == arr[i+1]`인 경우를 **별도 처리할 필요가 없음** — `<`, `>` 조건에서 자동으로 루프가 멈추므로 자연스럽게 `False`가 반환됨

### 4-2. 대안 — Two-pointer

왼쪽에서 올라오는 포인터와 오른쪽에서 올라오는 포인터가 **같은 인덱스에서 만나면** 그 지점이 봉우리라는 관찰을 이용할 수 있습니다.

```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        l, r = 0, n - 1
        while l + 1 < n and arr[l] < arr[l+1]:
            l += 1
        while r > 0 and arr[r-1] > arr[r]:
            r -= 1
        return 0 < l == r < n - 1
```

마지막 반환 조건 `0 < l == r < n - 1`이 이 풀이의 핵심으로, **"두 포인터가 같은 지점에서 만났고, 그 지점이 양 끝이 아니어야 한다"**는 요건을 한 줄로 표현합니다.

### 4-3. 기존 풀이에서 바로 정리할 수 있는 부분

원래 풀이 그대로 두더라도 다음 소소한 개선이 가능합니다.

- **`if` → `elif` 연결**: 첫 번째 `if`에서 `return`하거나 플래그를 바꾼 뒤에도 두 번째 `if`가 재실행됩니다. 실제 버그는 없지만(`increase`가 방금 막 `False`로 바뀌었으므로), `elif`로 묶으면 **의도가 명확**해지고 분기의 배타성이 드러납니다.
- `peak_found`는 `not increase`와 사실상 동치이므로, 루프가 끝난 뒤 **`return not increase`로 대체** 가능합니다(플래그 하나 절약).

---

## 정리

| 항목 | 기존 풀이 | Two-pass 개선안 |
|---|---|---|
| 시간 복잡도 | O(n) | O(n) |
| 공간 복잡도 | O(1) | O(1) |
| 상태 변수 | 2개 (`increase`, `peak_found`) | 0개 |
| 가독성 | 보통 | 좋음 |